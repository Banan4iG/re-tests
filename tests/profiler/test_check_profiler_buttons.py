import lackey
from re_tests_plugin import *
import firebird.driver as fdb

def test_check_profiler_buttons(open_connection):
    lackey.click("tools.png")
    lackey.click("text_profiler.png")
    lackey.click("start.png")
    result1 = lackey.exists("transparent_start.png")
    lackey.click("tree_plus.png")
    lackey.rightClick("icon_tables.png")
    lackey.click("tree_create_menu.png")
    lackey.click("text_Name_table.png")
    lackey.type("test")
    lackey.type("{TAB}")
    lackey.type("{b}")
    lackey.type("{b}")
    lackey.click("bt_OK.png")
    lackey.click("bt_commit.png")
    lackey.click("pause.png")
    result2 = lackey.exists("icon_profiler.png")
    lackey.click("resume.png")
    result3 = lackey.exists("transparent_resume.png")
    lackey.click("stop.png")
    lackey.click("bt_OK_blue.png")
    result4 = lackey.exists("transparent_stop.png")
    lackey.click("start.png")
    lackey.click("bt_cancel.png")
    lackey.click("discard.png")
    lackey.click("icon_cross.png")
    with fdb.connect("employee") as con:
        con.execute_immediate("DROP TABLE NEW_TABLE_1;")
        con.commit()
    assert result1 != None
    assert result2 != None
    assert result3 != None
    assert result4 != None