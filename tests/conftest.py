import pytest

from lepton.lib.common.config import Config
from tests.helpers import ConfName, Paths


@pytest.fixture
def config():
    """Return a factory that loads a Config from tests/data/config/."""

    def _config(name: ConfName) -> Config:
        return Config(Paths().data(name))

    return _config
