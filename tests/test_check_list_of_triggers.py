import lackey
from re_tests_plugin import *

def test_1(open_connection):
    lackey.click("tree_plus.png")
    name_of_the_group = "icon_tables.png"
    lackey.click(plus_find(name_of_the_group))
    lackey.doubleClick("tree_table_name_EMPLOYEE.png")
    lackey.click("tab_triggers.png")
    lackey.doubleClick("trigger_name.png")
    time.sleep(2)
    lackey.type("{ESC}")
    result = lackey.exists("trigger_name.png")
    lackey.rightClick("tab_table_EMPLOYEE_blue.png")
    lackey.click("bt_tab_close_all.png")
    assert result != None, "List of triggers is empty"
