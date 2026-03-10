from pathlib import Path
from typing import Optional

import tomlkit


class ConfBuilder:
    """Build a config TOML from scratch using a fluent DSL."""

    def __init__(self):
        self._doc = tomlkit.document()
        self._doc["lepton"] = tomlkit.table()

    def add_app(
        self, app_type: str, profile: str, cmd: str, exec_: Optional[str] = None
    ) -> "ConfBuilder":
        """Add an application that the user can execute."""
        apps = self._doc["lepton"].setdefault("apps", tomlkit.table())

        if app_type not in apps:
            apps[app_type] = tomlkit.table()

        entry = {"cmd": cmd}
        if exec_ is not None:
            entry["exec"] = exec_

        apps[app_type][profile] = entry

        return self

    def add_qube(self, name: str, apps: dict) -> "ConfBuilder":
        """Assign reusable configuration values to a qube."""
        qubes = self._doc["lepton"].setdefault("qube", tomlkit.table())
        qubes[name] = tomlkit.table()
        qubes[name]["apps"] = apps
        return self

    def add_templatevm(self, http_proxy: str, https_proxy: str) -> "ConfBuilder":
        """Assign TemplateVM configuration values."""
        common = self._doc["lepton"].setdefault("common", tomlkit.table())
        common["templatevms"] = {"http_proxy": http_proxy, "https_proxy": https_proxy}
        return self

    @classmethod
    def typical(cls) -> "ConfBuilder":
        """Return a builder preconfigured with the typical CONFIG values."""
        return (
            cls()
            .add_app("terminal", "default", "alacritty", "alacritty --command %s")
            .add_app("terminal", "graphics", "kitty", "kitty --command %s")
            .add_qube("email", {"terminal": "default"})
            .add_templatevm("http://127.0.0.1:8082", "http://127.0.0.1:8082")
        )

    def build(self, path: Path) -> Path:
        """Write the config to a temp file and return its path."""
        path = path / "config.toml"
        path.write_text(self._doc.as_string())
        return path
