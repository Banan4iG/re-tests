import lackey
from re_tests_plugin import *


def test_check_delete_button(open_connection):
    lackey.click("tools.png")
    lackey.click("tab_user_manager.png")
    lackey.click("bt_add.png")
    result = lackey.exists("text_add_user_visible.png")
    lackey.type("{TAB}")
    lackey.type("test")
    lackey.type("{TAB}")
    lackey.type("{TAB}")
    lackey.type("{TAB}")
    lackey.type("test")
    lackey.type("{TAB}")
    lackey.type("test")
    lackey.click("bt_OK.png")
    lackey.click("text_TEST.png")
    lackey.click("tree_delete_menu.png")
    lackey.click("bt_yes.png")
    lackey.click("icon_cross.png")
    assert result != None