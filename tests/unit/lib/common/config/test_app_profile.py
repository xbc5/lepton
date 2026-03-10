from lepton.lib.common.config import Config
from tests.conf_builder import ConfBuilder


class TestExec:
    def test_interpolates_args(self, typical_conf):
        """Test that it interpolates args into the exec template."""
        app = typical_conf.get_app_for("email", "terminal")
        assert app.exec("mutt") == "alacritty --command mutt"

    def test_optional(self, tmp_path):
        """Test that it loads an app without an exec template."""
        cfg = Config(
            ConfBuilder()
            .add_app("terminal", "default", "alacritty")
            .add_qube("email", {"terminal": "default"})
            .build(tmp_path)
        )
        app = cfg.get_app_for("email", "terminal")
        assert app.exec() is None


class TestCmd:
    def test_returns_cmd(self, typical_conf):
        """Test that it returns the correct cmd for a resolved app."""
        app = typical_conf.get_app_for("email", "terminal")
        assert app.cmd() == "alacritty"
