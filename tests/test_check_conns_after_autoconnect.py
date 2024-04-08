import lackey
import time
from re_tests_plugin import *

def test_1():
    lackey.rightClick("icon_conn.png")
    lackey.click("tree_create_duplicate.png")
    time.sleep(1)
    lackey.click("tools.png")
    lackey.click("tab_user_manager.png")
    time.sleep(1)
    lackey.click("button_down.png")
    lackey.type("{DOWN}{ENTER}")
    list_conn = list(lackey.findAll("icon_conn_open.png"))
    for conn in list_conn:
        lackey.doubleClick(conn)
    list_b = list(lackey.findAll("icon_conn.png"))
    b = max(list_b, key=lambda i: i.getTarget().getY())
    lackey.rightClick(b.getTarget())
    lackey.click("tree_remove_conn.png")
    lackey.type("{ENTER}")
    lackey.rightClick("icon_abstract_object.png")
    lackey.click("bt_tab_close_all.png")
    assert len(list_conn) == 2

