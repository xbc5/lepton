from tests.helpers import ConfName


def test_app_exec(config):
    """Test that it interpolates args into the exec template."""
    app = config(ConfName.TYPICAL).get_app_for("email", "terminal")
    assert app.exec("mutt") == "alacritty --command mutt"
