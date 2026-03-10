from tests.helpers import ConfName


def test_loads_config(config):
    """Test that it loads a config file without error."""
    cfg = config(ConfName.TYPICAL)
    assert cfg is not None
