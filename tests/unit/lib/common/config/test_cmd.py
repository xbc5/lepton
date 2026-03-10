from tests.helpers import ConfName


def test_app_cmd(config):
    """Test that it returns the correct cmd for a resolved app."""
    app = config(ConfName.TYPICAL).get_app_for("email", "terminal")
    assert app.cmd() == "alacritty"
