import lackey
from re_tests_plugin import *
import firebird.driver as fdb


def test_data_with_space(open_connection):
    with fdb.connect("employee") as con:
        con.execute_immediate("CREATE TABLE NEW_TABLE_1(\"TEST COL\" VARCHAR(50));")
        con.commit()
        con.execute_immediate("INSERT INTO NEW_TABLE_1 (\"TEST COL\")  VALUES (null);")
        con.commit()
    lackey.click("tree_plus.png")
    lackey.rightClick("icon_tables.png")
    lackey.click("tree_reload_menu.png")
    lackey.click(plus_find("icon_tables.png"))
    lackey.doubleClick("text_NEW_TABLE_1.png")
    lackey.click("tab_data.png")
    lackey.doubleClick("text_NULL_blue.png")
    lackey.type("a", lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE)
    lackey.type("PUBLIC")
    lackey.type(lackey.Key.ENTER)
    lackey.click("icon_commit.png")
    with fdb.connect("employee") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM NEW_TABLE_1;")
        result1 = cur.fetchone()
        cur.close()
    lackey.click("text_PUBLIC.png")
    lackey.click("bt_delete_record.png")
    lackey.click("icon_commit.png")
    with fdb.connect("employee") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM NEW_TABLE_1;")
        result2 = cur.fetchone()
        cur.close()
    lackey.click("icon_cross.png")
    with fdb.connect("employee") as con:
        con.execute_immediate("DROP TABLE NEW_TABLE_1;")
        con.commit()
    assert result1 == ('PUBLIC',)
    assert result2 == None