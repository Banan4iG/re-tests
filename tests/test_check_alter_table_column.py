import lackey
from re_tests_plugin import *
import firebird.driver as fdb


def test_check_constraints_spacebar(open_connection):
    with fdb.connect("employee") as con:
        con.execute_immediate("CREATE TABLE NEW_TABLE_1(PUBLIC int);")
        con.commit()
    lackey.click("tree_plus.png")
    lackey.rightClick("icon_tables.png")
    lackey.click("tree_reload_menu.png")
    lackey.click(plus_find("icon_tables.png"))
    lackey.doubleClick("text_NEW_TABLE_1.png")
    lackey.doubleClick("text_PUBLIC.png")
    lackey.type("{TAB}")
    lackey.type("a",lackey.Key.CTRL)
    lackey.type("TEST")
    lackey.click("bt_OK.png")
    lackey.click("bt_commit.png")
    result = lackey.exists("text_TEST.png")
    lackey.click("icon_cross.png")
    with fdb.connect("employee") as con:
        con.execute_immediate("DROP TABLE NEW_TABLE_1;")
        con.commit()
    assert result != None