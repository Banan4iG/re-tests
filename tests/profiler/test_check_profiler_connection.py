import lackey
from re_tests_plugin import *

def test_check_profiler_connection(open_connection):
    lackey.rightClick("icon_conn_open.png")
    lackey.click("tree_create_menu.png")
    lackey.doubleClick("icon_conn.png")
    lackey.click("tools.png")
    lackey.click("text_profiler.png")
    lackey.type("{TAB}")
    lackey.type(lackey.Key.SPACE)
    result1 = lackey.exists("text_Copy.png")
    lackey.type(lackey.Key.DOWN)
    lackey.type(lackey.Key.SPACE)
    lackey.click("text_127.png")
    result2 = lackey.exists("text_127_blue.png")
    lackey.click("text_127.png")
    lackey.click("icon_cross.png")
    lackey.rightClick("text_Copy.png")
    lackey.click("text_Disconnect.png")
    lackey.rightClick("text_Copy.png")
    lackey.click("tree_remove_conn.png")
    lackey.click("bt_yes.png")
    assert result1 != None
    assert result2 != None