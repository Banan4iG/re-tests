import time
import lackey
from re_tests_plugin import *


def test_transition_index(open_connection):
    lackey.click("tree_plus.png")
    name_of_the_group = "icon_tables.png"
    lackey.click(plus_find(name_of_the_group))
    lackey.doubleClick("tree_table_name_EMPLOYEE.png")
    lackey.click("indices.png")
    lackey.doubleClick("column_name_EMP_NO.png")
    result = lackey.exists("edit_index.png")
    time.sleep(4)
    lackey.click("bt_cancel.png")
    lackey.rightClick("tab_table_EMPLOYEE_blue.png")
    lackey.click("bt_tab_close_all.png")
    assert result != None
