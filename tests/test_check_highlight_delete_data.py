import lackey
from re_tests_plugin import *
import time

def test_1(open_connection):
    lackey.click("tree_plus.png")
    name_of_the_group = "icon_tables.png"
    lackey.click(plus_find(name_of_the_group))
    lackey.doubleClick("tree_table_name_EMPLOYEE.png")
    lackey.click("tab_data.png")
    time.sleep(2)
    lackey.click("data_field_1.png")
    lackey.click("icon_delete_record.png")
    result = lackey.exists("data_field_1_red.png")
    lackey.click("tab_columns.png")
    lackey.click("bt_No.png")
    lackey.rightClick("tab_table_EMPLOYEE_blue.png")
    lackey.click("bt_tab_close_all.png")
    assert result != None