from lepton.lib.common.config import Config
from tests.conf_builder import ConfBuilder


def test_loads_config(typical_conf):
    """Test that it loads a config file without error."""
    assert typical_conf is not None


class TestOptionality:
    def test_empty_lepton(self, tmp_path):
        """Test that it loads with only the root namespace."""
        assert Config(ConfBuilder().build(tmp_path)) is not None

    def test_without_apps(self, tmp_path):
        """Test that it loads without any apps."""
        cfg = Config(ConfBuilder().add_qube("email", {"terminal": "default"}).build(tmp_path))
        assert cfg._config.lepton.apps is None

    def test_without_qube(self, tmp_path):
        """Test that it loads without any qubes."""
        cfg = Config(ConfBuilder().add_app("terminal", "default", "alacritty").build(tmp_path))
        assert cfg._config.lepton.qube is None

    def test_without_common(self, tmp_path):
        """Test that it defaults common when absent."""
        assert Config(ConfBuilder().build(tmp_path)).common is not None

    def test_without_mgmt(self, tmp_path):
        """Test that it loads without the mgmt namespace."""
        assert Config(ConfBuilder().build(tmp_path))._config.lepton.mgmt is None
