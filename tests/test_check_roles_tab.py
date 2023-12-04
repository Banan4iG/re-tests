from unittest import result

import lackey
from re_tests_plugin import *

def test_check_roles_tab(open_connection):
    lackey.click("tools.png")
    lackey.click("tab_user_manager.png")
    lackey.click("tab_roles.png")
    lackey.click("bt_add.png")
    lackey.type("test")
    lackey.click("bt_OK.png")
    lackey.click("bt_commit.png")
    result = lackey.exists("text_roles_tab_visible.png")
    lackey.click("text_TEST.png")
    lackey.click("tree_delete_menu.png")
    lackey.click("bt_yes.png")
    lackey.click("icon_cross.png")
    assert result != None