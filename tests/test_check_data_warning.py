import lackey
from re_tests_plugin import *
import firebird.driver as fdb


def test_check_data_warning(lock_employee, open_connection):
    with fdb.connect("employee") as con:
        con.execute_immediate("CREATE TABLE NEW_TABLE_1(TEST_COL int);")
        con.commit()
    lackey.click("tree_plus.png")
    lackey.rightClick("icon_tables.png")
    lackey.click("tree_reload_menu.png")
    lackey.click(plus_find("icon_tables.png"))
    lackey.doubleClick("text_NEW_TABLE_1.png")
    lackey.click("tab_data.png")
    lackey.click("bt_insert_record.png")
    lackey.click("icon_commit_data.png")
    time.sleep(2)
    lackey.click("text_NULL_blue.png")
    lackey.click("bt_delete_record.png")
    lackey.click("tab_constraints.png")
    result1 = lackey.exists("text_apply_changes.png")
    lackey.click("text_Yes.png")
    lackey.click("icon_cross.png")
    assert result1 != None