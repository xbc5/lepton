from pathlib import Path

import pytest

from lepton.lib.config import Config

DATA_DIR = Path(__file__).parent / "data" / "config"

TYPICAL = "typical.toml"


@pytest.fixture
def config():
    """Return a factory that loads a Config from tests/data/config/."""
    def _config(name: str) -> Config:
        return Config(DATA_DIR / name)
    return _config
