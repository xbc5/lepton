def test_app_exec(typical_conf):
    """Test that it interpolates args into the exec template."""
    app = typical_conf.get_app_for("email", "terminal")
    assert app.exec("mutt") == "alacritty --command mutt"
