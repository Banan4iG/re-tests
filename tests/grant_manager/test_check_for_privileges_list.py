import lackey
from re_tests_plugin import *
import firebird.driver as fdb


def test_check_for_privileges_list():
    with fdb.connect("employee") as con:
        con.execute_immediate("""
CREATE OR ALTER FUNCTION NEW_FUNC
RETURNS VARCHAR(5)
AS
begin
  RETURN 'five';
end
""")
        con.execute_immediate("CREATE PACKAGE NEW_PACK AS BEGIN END;")
        con.execute_immediate("RECREATE PACKAGE BODY NEW_PACK AS BEGIN END;")
        con.commit()
    lackey.doubleClick("icon_conn.png")
    lackey.click("tools.png")
    lackey.click("tab_grant_manager.png")
    result1 = lackey.exists("text_SYSDBA_blue.png")
    lackey.click("text_Users.png")
    lackey.click("text_Roles.png")
    result2 = lackey.exists("list_roles_gm.png")
    lackey.click("text_Roles.png")
    lackey.click("text_Views.png")
    result3 = lackey.exists("text_PHONE_LIST_blue.png")
    lackey.click("text_Views.png")
    lackey.click("text_Triggers.png")
    result4 = lackey.exists("list_triggers_gm.png")
    lackey.click("text_Triggers.png")
    lackey.click("text_Procedures.png")
    result5 = lackey.exists("list_proc_gm.png")
    lackey.click("text_Procedures.png")
    lackey.click("text_Functions.png")
    result6 = lackey.exists("text_NEW_FUNC_blue.png")
    lackey.click("text_Functions.png")
    lackey.click("text_Packages.png")
    result7 = lackey.exists("text_NEW_PACK_blue.png")
    lackey.click("icon_cross.png")
    with fdb.connect("employee") as con:
        con.execute_immediate("DROP FUNCTION NEW_FUNC;")
        con.execute_immediate("DROP PACKAGE NEW_PACK;")
        con.commit()
    lackey.doubleClick("icon_conn_open.png")
    assert result1 != None
    assert result2 != None
    assert result3 != None
    assert result4 != None
    assert result5 != None
    assert result6 != None
    assert result7 != None