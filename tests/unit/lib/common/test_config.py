from tests.helpers import ConfName


def test_loads_config(config):
    """Test that it loads a config file without error."""
    cfg = config(ConfName.TYPICAL)
    assert cfg is not None


def test_app_cmd(config):
    """Test that it returns the correct cmd for a resolved app."""
    app = config(ConfName.TYPICAL).get_app_for("email", "terminal")
    assert app.cmd() == "alacritty"


def test_app_exec(config):
    """Test that it interpolates args into the exec template."""
    app = config(ConfName.TYPICAL).get_app_for("email", "terminal")
    assert app.exec("mutt") == "alacritty --command mutt"
