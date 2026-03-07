import tomllib
from pathlib import Path
from typing import Dict

from pydantic import BaseModel


# Pydantic models for config validation.

class AppConfig(BaseModel):
    cmd: str
    exec: str


class Domain(BaseModel):
    # Maps app type (e.g. "terminal") to a named profile (e.g. "default").
    apps: Dict[str, str]


class LeptonConfig(BaseModel):
    # Maps app type to a dict of named profiles, each with cmd and exec.
    apps: Dict[str, Dict[str, AppConfig]]
    domains: Dict[str, Domain]


class RootConfig(BaseModel):
    lepton: LeptonConfig


class App:
    """Represents a resolved application, providing its command and exec template."""

    def __init__(self, config: AppConfig):
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
        self._config = RootConfig(**raw)

    def get_app_for(self, domain: str, app_type: str) -> App:
        """Return the App configured for the given domain and app type."""
        profile = self._config.lepton.domains[domain].apps[app_type]
        app_config = self._config.lepton.apps[app_type][profile]
        return App(app_config)
