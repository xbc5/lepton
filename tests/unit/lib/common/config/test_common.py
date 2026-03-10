def test_common_templatevm_proxies(typical_conf):
    """Test that it parses the common templatevm proxy settings."""
    common = typical_conf.common
    assert common.templatevms.http_proxy == "http://127.0.0.1:8082"
    assert common.templatevms.https_proxy == "http://127.0.0.1:8082"
