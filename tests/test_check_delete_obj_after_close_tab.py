import lackey
from re_tests_plugin import *
import firebird.driver as fdb

def test_1(lock_employee, open_connection):
    script = """
CREATE OR ALTER FUNCTION NEW_FUNC
RETURNS VARCHAR(5)
AS
begin
  RETURN 'five';
end
"""

    with fdb.connect('employee') as con:
        con.execute_immediate(script)
        con.commit()
    
    lackey.click("tree_plus.png")
    lackey.rightClick("icon_functions.png")
    lackey.click("tree_reload_menu.png")
    lackey.click(plus_find("icon_functions.png"))
    lackey.doubleClick("func_NEW_FUNC.png")
    lackey.rightClick("func_NEW_FUNC_blue.png")
    lackey.click("tree_delete_menu.png")
    result1 = lackey.exists("error_message_delete_func.png")
    lackey.click("bt_OK_blue.png")
    lackey.rightClick("tab_new_func.png")
    lackey.click("bt_tab_close_all.png")
    lackey.rightClick("func_NEW_FUNC_blue.png")
    lackey.click("tree_delete_menu.png")
    result2 = lackey.exists("text_success.png")
    lackey.click("bt_commit.png")
    assert result1 != None
    assert result2 != None