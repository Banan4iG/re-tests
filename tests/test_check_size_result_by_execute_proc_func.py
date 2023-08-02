import lackey
from re_tests_plugin import *
import firebird.driver as fdb


def test_check_proc(open_connection):
    lackey.click("tree_plus.png")
    lackey.click(plus_find("icon_procedures.png"))
    lackey.rightClick("proc_ALL_LANGS.png")
    lackey.click("tree_edit_menu.png")
    lackey.click("bt_execute.png")
    lackey.click("bt_execute_big.png")
    result1 = lackey.exists("result_set_proc_ALL_LANGS.png")
    lackey.click("tab_output.png")
    result2 =  lackey.exists("output_proc_ALL_LANGS.png")
    lackey.click("close.png")
    lackey.click("bt_cancel.png")
    assert result1 != None
    assert result2 != None

def test_check_func(open_connection):
    script = """
CREATE OR ALTER FUNCTION NEW_FUNC
RETURNS VARCHAR(5)
AS
begin
  RETURN 'five';
end
"""

    with fdb.connect(database='localhost:employee.fdb', user=ADMIN_NAME, password=ADMIN_PASSWORD) as con:
        con.execute_immediate(script)
        con.commit()
    
    lackey.click("tree_plus.png")
    lackey.rightClick("icon_functions.png")
    lackey.click("tree_reload_menu.png")
    lackey.click(plus_find("icon_functions.png"))
    lackey.rightClick("func_NEW_FUNC.png")
    lackey.click("tree_edit_menu.png")
    lackey.click("bt_execute.png")
    lackey.click("bt_execute_big.png")
    result1 = lackey.exists("result_set_func_NEW_FUNC.png")
    lackey.click("tab_output.png")
    result2 =  lackey.exists("output_func_NEW_FUNC.png")
    lackey.click("close.png")
    lackey.click("bt_cancel.png")
    with fdb.connect(database='localhost:employee.fdb', user=ADMIN_NAME, password=ADMIN_PASSWORD) as con:
        con.execute_immediate("DROP FUNCTION NEW_FUNC")
        con.commit()
    assert result1 != None
    assert result2 != None