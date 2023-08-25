import lackey
from re_tests_plugin import *

def test_check_with_alias(open_connection):
    lackey.click("tab_query_editor.png")
    lackey.click("tab_query_editor_text.png")
    lackey.type("select * from EMPLOYEE e join DEPARTMENT d on e.")
    result1 = list(lackey.findAll("icon_table_field.png"))
    lackey.type("DEPT_NO=d.")
    result2 = list(lackey.findAll("icon_table_field.png"))
    lackey.type("a", lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE)
    assert len(result1) == 4 
    assert len(result2) == 4 