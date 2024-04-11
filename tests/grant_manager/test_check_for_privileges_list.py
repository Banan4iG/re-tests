import lackey
from re_tests_plugin import *
import firebird.driver as fdb


def test_check_for_privileges_list(open_connection):
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
    lackey.rightClick("icon_conn_open.png")
    lackey.click("tree_reload_menu.png")
    lackey.click("tools.png")
    lackey.click("tab_grant_manager.png")
    result1 = lackey.exists("text_SYSDBA_blue.png")
    list_b = list(lackey.findAll("button_down.png"))
    b = max(list_b, key=lambda i: i.getTarget().getY())
    b = b.getTarget()
    lackey.click(b)
    lackey.type("{DOWN}")
    if srv_version == "Firebird":
        result2 = lackey.exists("list_roles_gm_fb.png")
    else:
        result2 = lackey.exists("list_roles_gm.png")

    results = []
    for obj in ["text_PHONE_LIST_blue.png", "list_triggers_gm.png", "list_proc_gm.png", "text_NEW_FUNC_blue.png", "text_NEW_PACK_blue.png"]:
        lackey.click(b)
        lackey.type("{DOWN}")
        results.append(lackey.exists(obj))
    lackey.click("icon_cross.png")
    with fdb.connect("employee") as con:
        con.execute_immediate("DROP FUNCTION NEW_FUNC;")
        con.execute_immediate("DROP PACKAGE NEW_PACK;")
        con.commit()
    assert result1 != None
    assert result2 != None
    assert results != [None, None, None, None, None]