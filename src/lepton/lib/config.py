import tomllib
from pathlib import Path
from typing import Dict

from pydantic import BaseModel, validator


# Pydantic models for config validation.


class AppModel(BaseModel):
    """Represents a typical app."""

    cmd: str
    exec: str


class QubeModel(BaseModel):
    """Represents a single qube."""

    name: str
    apps: Dict[str, str]


class LeptonModel(BaseModel):
    """A simple, future-proof namespace."""

    apps: Dict[str, Dict[str, AppModel]]
    qubes: Dict[str, QubeModel]

    @validator("qubes", pre=True)
    def inject_names(cls, qubes):
        # Inject the TOML key as the qube name, because the model needs it.
        return {k: {**v, "name": k} for k, v in qubes.items()}


class RootModel(BaseModel):
    """The entire configuration model."""

    lepton: LeptonModel


class App:
    """Represents a resolved application, providing its command and exec template."""

    def __init__(self, config: AppModel):
        self._config = config

    def cmd(self) -> str:
        """Return the raw command string."""
        return self._config.cmd

    def exec(self, *args) -> str:
        """Interpolate args into the exec template and return the result."""
        return self._config.exec % args if args else self._config.exec


class Config:
    """Loads and validates /etc/config.toml, providing app resolution for domains."""

    CONFIG_PATH = Path("/etc/config.toml")

    def __init__(self):
        with open(self.CONFIG_PATH, "rb") as f:
            raw = tomllib.load(f)
        self._config = RootModel(**raw)

    def get_app_for(self, domain: str, app_type: str) -> App:
        """Return the App configured for the given domain and app type."""
        profile = self._config.lepton.qubes[domain].apps[app_type]
        app_config = self._config.lepton.apps[app_type][profile]
        return App(app_config)
