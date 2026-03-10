from lepton.lib.common.config import Config
from tests.conf_builder import ConfBuilder


def test_returns_named_qube(tmp_path):
    """Test that it returns the qube by name."""
    cfg = Config(
        ConfBuilder()
        .add_qube("email", apps={"terminal": "default"})
        .build(tmp_path)
    )
    assert cfg._config.lepton.get_qube("email").name == "email"


def test_falls_back_to_all(tmp_path):
    """Test that it falls back to 'all' when the name is missing."""
    cfg = Config(
        ConfBuilder()
        .add_qube("all", apps={"terminal": "default"})
        .build(tmp_path)
    )
    assert cfg._config.lepton.get_qube("email").name == "all"


def test_returns_none_without_qubes(tmp_path):
    """Test that it returns None when no qubes are defined."""
    cfg = Config(ConfBuilder().build(tmp_path))
    assert cfg._config.lepton.get_qube("email") is None


def test_returns_none_without_match(tmp_path):
    """Test that it returns None when neither name nor 'all' exist."""
    cfg = Config(
        ConfBuilder()
        .add_qube("web", apps={"terminal": "default"})
        .build(tmp_path)
    )
    assert cfg._config.lepton.get_qube("email") is None
