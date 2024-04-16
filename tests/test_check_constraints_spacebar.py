import lackey
from re_tests_plugin import *
import firebird.driver as fdb


def test_check_constraints_spacebar(lock_employee, open_connection):
    with fdb.connect("employee") as con:
        con.execute_immediate("CREATE TABLE NEW_TABLE_1(\"TEST COMMENT\" int);")
        con.commit()
    lackey.click("tree_plus.png")
    lackey.rightClick("icon_tables.png")
    lackey.click("tree_reload_menu.png")
    lackey.click(plus_find("icon_tables.png"))
    lackey.doubleClick("text_NEW_TABLE_1.png")
    lackey.click("tab_constraints.png")
    lackey.click("bt_insert_constraint.png")
    lackey.click("text_PRIMARY.png")
    lackey.click("text_UNIQUE.png")
    lackey.doubleClick("text_TEST_COMMENT_CAPS.png")
    lackey.click("bt_OK.png")
    result1 = lackey.exists("text_success.png")
    lackey.click("bt_commit.png")
    result2 = lackey.exists("text_UQ_.png")
    lackey.click("icon_cross.png")
    assert result1 != None
    assert result2 != None