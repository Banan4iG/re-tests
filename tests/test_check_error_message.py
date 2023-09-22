import lackey
from re_tests_plugin import *

def test_check_after_close_result_set(open_connection):
    lackey.click("tab_query_editor.png")
    lackey.click("tab_query_editor_text.png")
    lackey.type("select * from employee")
    lackey.click("icon_execute_query.png")
    lackey.type("a", lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE)
    lackey.rightClick("tab_result_set.png")
    lackey.click("bt_tab_close_all.png")
    lackey.click("icon_visible_result_set_columns.png")
    result = lackey.exists("error_message_result_set.png")
    lackey.click("bt_OK_blue.png")
    assert result != None