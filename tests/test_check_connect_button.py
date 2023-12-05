import lackey
from re_tests_plugin import *

def test_check_connect_button():
    lackey.click("tools.png")
    lackey.click("tab_user_manager.png")
    lackey.click("bt_connect.png")
    lackey.click("bt_OK.png")
    result = lackey.exists("text_connect_button_visible.png")
    lackey.click("icon_cross.png")
    assert result != None