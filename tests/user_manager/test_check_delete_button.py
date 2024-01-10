import lackey
from re_tests_plugin import *


def test_check_delete_button(open_connection):
    lackey.click("tools.png")
    lackey.click("tab_user_manager.png")
    lackey.click("bt_add.png")
    result1 = lackey.exists("text_add_user_visible.png")
    lackey.type("test{TAB}test{TAB}{TAB}{TAB}test{TAB}test")
    lackey.click("bt_OK.png")
    result2 = lackey.exists("text_TEST.png")
    lackey.click("text_TEST.png")
    lackey.click("tree_delete_menu.png")
    lackey.click("bt_yes.png")
    lackey.rightClick("tab_user_manager_blue.png")
    lackey.click("bt_tab_close.png")
    assert result1 != None
    assert result2 != None