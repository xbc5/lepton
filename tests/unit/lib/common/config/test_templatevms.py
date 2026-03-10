from lepton.lib.common.config import Config
from tests.conf_builder import ConfBuilder


def test_http_proxy(typical_conf):
    """Test that it parses the http_proxy setting."""
    assert typical_conf.common.templatevms.http_proxy == "http://127.0.0.1:8082"


def test_https_proxy(typical_conf):
    """Test that it parses the https_proxy setting."""
    assert typical_conf.common.templatevms.https_proxy == "http://127.0.0.1:8082"


class TestOptionality:
    def test_without_common(self, tmp_path):
        """Test that it loads without the common namespace."""
        cfg = Config(ConfBuilder().build(tmp_path))
        assert cfg.common is None

    def test_without_templatevms(self, tmp_path):
        """Test that it loads common without templatevms."""
        cfg = Config(ConfBuilder().add_app("terminal", "default", "alacritty").build(tmp_path))
        assert cfg.common is None
