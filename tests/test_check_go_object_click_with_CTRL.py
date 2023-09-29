import lackey
from re_tests_plugin import *

def check(use_cancel=True):
    lackey.click("text_employee_highlight.png", lackey.Key.CTRL)
    if use_cancel:
        lackey.click("bt_cancel.png")
    result = lackey.exists("tab_table_EMPLOYEE_blue.png")
    lackey.rightClick("tab_table_EMPLOYEE_blue.png")
    lackey.click("bt_tab_close_all.png")
    return result


def test_check_in_create_window(open_connection):
    lackey.click("tree_plus.png")
    lackey.rightClick("icon_views.png")
    lackey.click("tree_create_menu.png")
    tab_ddl = lackey.exists("tab_DDL.png")
    lackey.click(tab_ddl)
    lackey.click(tab_ddl.getTarget().below(50))
    lackey.type("a", lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE)
    script = """CREATE OR ALTER VIEW NEW_VIEW_1 
AS 
SELECT emp_no FROM employee;
"""
    lackey.App.setClipboard(script)
    lackey.type("v", lackey.Key.CTRL)
    result = check()  
    assert result != None
    

def test_check_in_edit_window(open_connection):
    lackey.click("tree_plus.png")
    plus = plus_find("icon_procedures.png")
    lackey.click(plus)
    lackey.rightClick("proc_DELETE_EMPLOYEE.png")
    lackey.click("tree_edit_menu.png")
    result = check()
    mouse = lackey.Mouse()
    mouse.move(plus)
    lackey.wheel(lackey.Mouse.WHEEL_UP, 10)
    assert result != None

def test_check_in_tab(open_connection):
    lackey.click("tree_plus.png")
    plus = plus_find("icon_procedures.png")
    lackey.click(plus)
    lackey.doubleClick("proc_DELETE_EMPLOYEE.png")
    result = check(False)
    mouse = lackey.Mouse()
    mouse.move(plus)
    lackey.wheel(lackey.Mouse.WHEEL_UP, 10)
    assert result != None