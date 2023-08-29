import lackey
from re_tests_plugin import *
import firebird.driver as fdb


def init_alter(icon):
    lackey.click("tree_plus.png")
    lackey.rightClick(icon)
    lackey.click("tree_reload_menu.png")
    lackey.click(plus_find(icon))

def click_tab_comment(object):
    lackey.rightClick(object)
    lackey.click("tree_delete_menu.png")
    result = len(list(lackey.findAll("text_success.png")))
    lackey.click("bt_commit.png")
    try:
        with fdb.connect('employee') as con:
            con.execute_immediate("DROP TRIGGER NEW_TRIGGER")
            con.commit()
    except Exception as e:
        s = str(e)
    assert result == 1
    assert "-Trigger NEW_TRIGGER not found" in s

def test_drop_trigger_for_ddl(open_connection):
    script = """
CREATE OR ALTER TRIGGER NEW_TRIGGER
ACTIVE BEFORE ANY DDL STATEMENT POSITION 0
AS
BEGIN
END
"""
    with fdb.connect('employee') as con:
        con.execute_immediate(script)
        con.commit()
    init_alter("icon_triggers_for_ddl.png")
    click_tab_comment("trigger_for_DDL_NEW_TRIGGER.png")
    


def test_drop_trigger_for_db(open_connection):
    script = """
CREATE OR ALTER TRIGGER NEW_TRIGGER
ACTIVE ON CONNECT POSITION 0
AS
BEGIN
END
"""
    with fdb.connect('employee') as con:
        con.execute_immediate(script)
        con.commit()
    init_alter("icon_triggers_for_db.png")
    click_tab_comment("trigger_for_DB_NEW_TRIGGER.png")