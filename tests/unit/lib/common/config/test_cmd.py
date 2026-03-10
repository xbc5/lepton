def test_app_cmd(typical_conf):
    """Test that it returns the correct cmd for a resolved app."""
    app = typical_conf.get_app_for("email", "terminal")
    assert app.cmd() == "alacritty"
