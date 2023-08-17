import lackey 
from re_tests_plugin import *

def test_1(open_connection):
    #open tabs
    lackey.click("tree_plus.png")
    name_of_the_group = "icon_tables.png"
    lackey.click(plus_find(name_of_the_group))
    lackey.doubleClick("tree_table_name_EMPLOYEE.png")
    lackey.click("tools.png")
    lackey.click("trace_manager.png")
    
    #close tabs with middle button
    mouse = lackey.Mouse()
    mouse.click(lackey.exists("tab_trace_manager_blue.png").getTarget(), button=mouse.MIDDLE)
    mouse.click(lackey.exists("tab_table_EMPLOYEE_blue.png").getTarget(), button=mouse.MIDDLE)
    mouse.click(lackey.exists("tab_query_editor_blue.png").getTarget(), button=mouse.MIDDLE)

    result1 = lackey.exists("tab_trace_manager_blue.png")
    result2 = lackey.exists("tab_table_EMPLOYEE_blue.png")
    result3 = lackey.exists("tab_query_editor_blue.png")

    assert result1 == None
    assert result2 == None
    assert result3 == None