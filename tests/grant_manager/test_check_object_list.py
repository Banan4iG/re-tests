import lackey
from re_tests_plugin import *
import firebird.driver as fdb


def test_check_object_list():
    with fdb.connect("employee") as con:
        con.execute_immediate("CREATE GLOBAL TEMPORARY TABLE NEW_TABLE (TETS BIGINT) ON COMMIT DELETE ROWS;")
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
    lackey.click("bt_refresh.PNG")
    result1 = len(list(lackey.findAll("icon_tables.png")))
    lackey.click("text_Tables.png")
    lackey.click("checkbox_Tables.png")
    lackey.click("user_SYSDBA_blue.png")
    result2 = len(list(lackey.findAll("icon_tables.png")))
    result3 = len(list(lackey.findAll("icon_gtt.png")))
    lackey.click("text_Global_Views.png")
    lackey.click("checkbox_Global.png")
    lackey.click("user_SYSDBA_blue.png")
    result4 = len(list(lackey.findAll("icon_gtt.png")))
    result5 = len(list(lackey.findAll("icon_views.png")))
    lackey.click("text_Views_Procedures.png")
    lackey.click("checkbox_Views.png")
    lackey.click("user_SYSDBA_blue.png")
    result6 = len(list(lackey.findAll("icon_views.png")))
    result7 = len(list(lackey.findAll("icon_procedures.png")))
    lackey.click("text_Procedures_Functions.png")
    lackey.click("checkbox_Procedures.png")
    lackey.click("user_SYSDBA_blue.png")
    result8 = len(list(lackey.findAll("icon_procedures.png")))
    result9 = len(list(lackey.findAll("icon_functions.png")))
    lackey.click("text_Functions_Packages.png")
    lackey.click("checkbox_Functions.png")
    lackey.click("user_SYSDBA_blue.png")
    result10 = len(list(lackey.findAll("icon_functions.png")))
    result11 = len(list(lackey.findAll("icon_packages.png")))
    lackey.click("text_Packages_Sequences.png")
    lackey.click("checkbox_Packages.png")
    lackey.click("user_SYSDBA_blue.png")
    result12 = len(list(lackey.findAll("icon_packages.png")))
    result13 = len(list(lackey.findAll("icon_sequences.png")))
    lackey.click("text_Sequences_Exceptions.png")
    lackey.click("checkbox_Sequences.png")
    lackey.click("user_SYSDBA_blue.png")
    result14 = len(list(lackey.findAll("icon_sequences.png")))
    result15 = len(list(lackey.findAll("icon_exceptions.png")))
    lackey.click("text_Exceptions_Empty.png")
    lackey.click("checkbox_Exceptions.png")
    lackey.click("user_SYSDBA_blue.png")
    result16 = len(list(lackey.findAll("icon_exceptions.png")))
    lackey.click("icon_cross.png")
    with fdb.connect("employee") as con:
        con.execute_immediate("DROP TABLE NEW_TABLE;")
        con.execute_immediate("DROP FUNCTION NEW_FUNC;")
        con.execute_immediate("DROP PACKAGE NEW_PACK;")
        con.commit()
    lackey.doubleClick("icon_conn_open.png")
    assert result1 == 10
    assert result2 == 0
    assert result3 == 1
    assert result4 == 0
    assert result5 == 1
    assert result6 == 0
    assert result7 == 10
    assert result8 == 0
    assert result9 == 1
    assert result10 == 0
    assert result11 == 1
    assert result12 == 0
    assert result11 == 1
    assert result12 == 0
    assert result13 == 2
    assert result14 == 0
    assert result15 == 5
    assert result16 == 0