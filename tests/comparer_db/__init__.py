import lackey
from re_tests_plugin import *

def create_duplicate_compare():
    lackey.rightClick("icon_conn_open.png")
    lackey.click("tree_create_menu.png")
    lackey.doubleClick("icon_conn.png")
    lackey.click("tools.png")
    lackey.click("comparer.png")
    lackey.click("text_Source.png")
    lackey.type("{DOWN}")
    lackey.type("{ENTER}")
    lackey.click("button_arrows.png")
    lackey.type("{TAB}")
    lackey.type("{TAB}")
    lackey.type(lackey.Key.SPACE)
    lackey.click("button_compare.png")
    time.sleep(2)
    lackey.click("bt_OK_blue.png")
def disconnect_delete_duplicate():
    lackey.rightClick("text_Copy.png")
    lackey.click("text_Disconnect.png")
    time.sleep(1)
    lackey.rightClick("text_Copy.png")
    lackey.click("tree_remove_conn.png")
    lackey.click("bt_yes.png")
