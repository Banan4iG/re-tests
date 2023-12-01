from unittest import result

import lackey
from re_tests_plugin import *

def test_check_delete_button():
    lackey.click("tools.png")
    lackey.click("tab_user_manager.png")
    lackey.click("bt_connect.png")
    lackey.click("bt_OK.png")
    lackey.click("bt_add.png")
    lackey.type("{TAB}")
    lackey.type("test")
    lackey.type("{TAB}")
    lackey.type("test")
    lackey.type("{TAB}")
    lackey.type("test")
    lackey.type("{TAB}")
    lackey.type("test")
    lackey.type("{TAB}")
    lackey.type("test")
    lackey.type("{TAB}")
    lackey.type("test")
    lackey.type("{TAB}")
    lackey.type("1")
    lackey.type("{TAB}")
    lackey.type("1")
    lackey.click("bt_OK.png")
    lackey.click("text_TEST.png")
    lackey.click("tree_delete_menu.png")
    lackey.click("bt_yes.png")
    assert result != None