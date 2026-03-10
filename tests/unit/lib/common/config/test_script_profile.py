from lepton.lib.common.config import Config
from tests.conf_builder import ConfBuilder


class TestOptionality:
    def test_without_scripts(self, tmp_path):
        """Test that it loads without any scripts."""
        cfg = Config(ConfBuilder().build(tmp_path))
        assert cfg._config.lepton.scripts is None

    def test_without_qube_scripts(self, tmp_path):
        """Test that it loads a qube without scripts."""
        cfg = Config(
            ConfBuilder()
            .add_qube("email", apps={"terminal": "default"})
            .build(tmp_path)
        )
        assert cfg._config.lepton.qube["email"].scripts is None

    def test_without_qube_apps(self, tmp_path):
        """Test that it loads a qube without apps."""
        cfg = Config(
            ConfBuilder()
            .add_script("proton-bridge", "default")
            .add_qube("email", scripts={"proton-bridge": "default"})
            .build(tmp_path)
        )
        assert cfg._config.lepton.qube["email"].apps is None
