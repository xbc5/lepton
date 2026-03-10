from lepton.lib.common.config import Config
from tests.conf_builder import ConfBuilder


def test_http_proxy(typical_conf):
    """Test that it parses the http_proxy setting."""
    assert typical_conf.common.templatevms.http_proxy == "http://127.0.0.1:8082"


def test_https_proxy(typical_conf):
    """Test that it parses the https_proxy setting."""
    assert typical_conf.common.templatevms.https_proxy == "http://127.0.0.1:8082"


class TestDefaults:
    def test_default_http_proxy(self, tmp_path):
        """Test that it defaults http_proxy when common is absent."""
        cfg = Config(ConfBuilder().build(tmp_path))
        assert cfg.common.templatevms.http_proxy == "http://127.0.0.1:8082"

    def test_default_https_proxy(self, tmp_path):
        """Test that it defaults https_proxy when common is absent."""
        cfg = Config(ConfBuilder().build(tmp_path))
        assert cfg.common.templatevms.https_proxy == "http://127.0.0.1:8082"
