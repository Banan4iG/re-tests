import lackey
from re_tests_plugin import *


def test_check_delete_button(open_connection):
    lackey.click("tools.png")
    lackey.click("tab_user_manager.png")
    lackey.click("bt_add.png")
    lackey.type("{TAB}")
    lackey.type("a", lackey.Key.CTRL)
    lackey.type("test")
    lackey.click("text_input_password.png")
    lackey.type("test{TAB}{TAB}test{TAB}test{TAB}test")
    lackey.click("bt_OK.png")
    lackey.click("bt_commit.png")
    result2 = lackey.exists("text_TEST.png")
    lackey.click("text_TEST.png")
    lackey.click("tree_delete_menu.png")
    lackey.click("bt_commit.png")
    lackey.rightClick("tab_user_manager_blue.png")
    lackey.click("bt_tab_close.png")
    assert result2 != None