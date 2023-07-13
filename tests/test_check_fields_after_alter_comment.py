import lackey
from re_tests_plugin import *

def click_comment():
    lackey.SettingsMaster.MinSimilarity = 0.93
    lackey.click("tab_comment.png")
    lackey.SettingsMaster.MinSimilarity = 0.97

def test_1(open_connection):
    lackey.click("tree_plus.png")
    name_of_the_group = "icon_tables.png"
    lackey.click(plus_find(name_of_the_group))
    lackey.doubleClick("tree_table_name_EMPLOYEE.png")
    click_comment()
    mouse = lackey.Mouse()
    lackey.click(mouse.getPos().below(100))
    lackey.type("test comment")
    lackey.click("icon_commit.png")
    lackey.click("tab_columns.png")
    result1 = lackey.exists("table_EMPLOYEE_list_of_columns.png")
    lackey.click("tab_constraints.png")
    result2 = lackey.exists("table_EMPLOYEE_list_of_constraints.png")
    click_comment()
    lackey.type("a", lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE)
    lackey.click("icon_commit.png")
    lackey.rightClick("tab_table_EMPLOYEE_blue.png")
    lackey.click("bt_tab_close_all.png")
    assert result1 != None
    assert result2 != None
