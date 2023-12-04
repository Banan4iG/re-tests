from unittest import result

import lackey
from re_tests_plugin import *

def test_check_edit_button(open_connection):
    lackey.click("tools.png")
    lackey.click("tab_user_manager.png")
    lackey.click("text_SYSDBA.png")
    lackey.click("tree_edit_menu.png")
    result = lackey.exists("text_edit_user_visible.png")
    lackey.click("bt_OK.png")
    lackey.rightClick("tab_user_manager_blue.png")
    lackey.click("bt_tab_close.png")
    assert result != None