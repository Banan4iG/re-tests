import lackey
from re_tests_plugin import *

def init_create(icon):
    lackey.click("tree_plus.png")
    lackey.rightClick(icon)
    lackey.click("tree_create_menu.png")

def finish_create():
    lackey.click("bt_OK.png")
    result1 = lackey.exists("text_success.png")
    result2 = lackey.exists("text_test_table.png")
    lackey.click("bt_rollback.png")
    lackey.click("bt_cancel.png")
    lackey.click("bt_YES.png")
    assert result1 != None
    assert result2 != None

def test_create_table(open_connection):
    init_create("icon_tables.png")
    lackey.type("a", lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE)
    lackey.type("TEST TABLE")
    lackey.click(lackey.exists("table_colum_Name.png").getTarget().below(20))
    lackey.type("test")
    lackey.click(lackey.exists("table_colum_Datatype.png").getTarget().below(20))
    lackey.click("datatype_BIGINT.png")
    finish_create()

def test_create_gtt(open_connection):
    init_create("icon_gtt.png")
    lackey.type("a", lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE)
    lackey.type("TEST TABLE")
    lackey.SettingsMaster.MinSimilarity = 0.96
    lackey.click(lackey.exists("table_colum_Name.png").getTarget().below(20))
    lackey.SettingsMaster.MinSimilarity = 0.97
    lackey.type("test")
    lackey.click(lackey.exists("table_colum_Datatype.png").getTarget().below(20))
    lackey.click("datatype_BIGINT.png")
    finish_create()