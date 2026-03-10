from tests.helpers import ConfName


def test_common_templatevm_proxies(config):
    """Test that it parses the common templatevm proxy settings."""
    common = config(ConfName.TYPICAL).common
    assert common.templatevm.http_proxy == "http://127.0.0.1:8082"
    assert common.templatevm.https_proxy == "http://127.0.0.1:8082"
