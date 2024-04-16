import lackey
from re_tests_plugin import *


vars = Variables()
ver = vars.get_version
srv_ver = vars.get_srv_version

@pytest.mark.skipif((not (ver == "5.0" and srv_ver == "RedDatabase")), reason="Not supported")
def test_check_cursor(open_connection):
    lackey.click("tree_plus.png")
    lackey.rightClick("icon_ts.png")
    lackey.click("tree_create_menu.png")
    lackey.click("text_file_ts.png")
    lackey.type("test_file.ts")
    lackey.click("bt_OK.png")
    result1 = lackey.exists("text_success.png")
    result2 = lackey.exists("text_test_file.ts.png")
    lackey.click("bt_rollback.png")
    lackey.click("bt_cancel.png")
    lackey.click("bt_YES.png")
    assert result1 != None
    assert result2 != None