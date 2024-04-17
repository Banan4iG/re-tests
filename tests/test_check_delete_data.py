import lackey
from re_tests_plugin import *
import firebird.driver as fdb


def test_check_delete_data(lock_employee, open_connection):
    with fdb.connect("employee") as con:
        con.execute_immediate("CREATE TABLE NEW_TABLE_1(TEST_COL VARCHAR(10))")
        con.commit()
        con.execute_immediate("INSERT INTO NEW_TABLE_1 VALUES('PUBLIC')")
        con.commit()
    lackey.click("tree_plus.png")
    lackey.rightClick("icon_tables.png")
    lackey.click("tree_reload_menu.png")
    lackey.click(plus_find("icon_tables.png"))
    lackey.doubleClick("text_NEW_TABLE_1.png")
    lackey.click("tab_data.png")
    lackey.click("text_PUBLIC.PNG")
    lackey.click("icon_delete_record.png")
    lackey.click("icon_commit_data.png")
    time.sleep(1)
    result1 = lackey.exists("text_PUBLIC.PNG")
    lackey.click("icon_cross.png")
    with fdb.connect("employee") as con:
        cur = con.cursor()
        cur.execute("SELECT * from NEW_TABLE_1")
        result2 = cur.fetchall()
    assert result1 == None
    assert result2 == []