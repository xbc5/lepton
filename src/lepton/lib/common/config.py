import tomllib
from pathlib import Path
from typing import Dict, Optional

from pydantic import BaseModel, validator


# Pydantic models for config validation.


class AppModel(BaseModel):
    """Represents a typical app."""

    cmd: str
    exec: Optional[str] = None


class QubeModel(BaseModel):
    """Represents a single qube."""

    name: str
    apps: Optional[Dict[str, str]] = None
    scripts: Optional[Dict[str, str]] = None


class TemplateVmModel(BaseModel):
    """Proxy settings pushed to template VMs."""

    http_proxy: str = "http://127.0.0.1:8082"
    https_proxy: str = "http://127.0.0.1:8082"


class CommonModel(BaseModel):
    """Non-sensitive configuration shared with every domain."""

    templatevms: TemplateVmModel = TemplateVmModel()


class MgmtModel(BaseModel):
    """Potentially sensitive configuration for management domains only."""

    pass


class LeptonModel(BaseModel):
    """A simple, future-proof namespace."""

    apps: Optional[Dict[str, Dict[str, AppModel]]] = None
    scripts: Optional[Dict[str, Dict[str, dict]]] = None
    qube: Optional[Dict[str, QubeModel]] = None
    common: CommonModel = CommonModel()
    mgmt: Optional[MgmtModel] = None

    def get_qube(self, name: str) -> Optional[QubeModel]:
        """Return the qube by name, falling back to 'all', then None."""
        if self.qube is None:
            return None
        return self.qube.get(name) or self.qube.get("all")

    @validator("qube", pre=True)
    def inject_names(cls, qube):
        # Inject the qube name (e.g., "foo" from lepton.qube.foo).
        if qube is None:
            return None
        return {k: {**v, "name": k} for k, v in qube.items()}


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
    """Loads and validates a config TOML, providing app resolution for qubes."""

    DEFAULT_PATH = Path("/etc/config.toml")

    def __init__(self, path: Path = DEFAULT_PATH):
        if path.exists():
            with open(path, "rb") as f:
                raw = tomllib.load(f)
        else:
            raw = {"lepton": {}}
        self._config = RootModel(**raw)

    @property
    def common(self) -> CommonModel:
        """Return the common namespace."""
        return self._config.lepton.common

    def get_app_for(self, domain: str, app_type: str) -> App:
        """Return the App configured for the given domain and app type."""
        profile = self._config.lepton.qube[domain].apps[app_type]
        app_config = self._config.lepton.apps[app_type][profile]
        return App(app_config)
