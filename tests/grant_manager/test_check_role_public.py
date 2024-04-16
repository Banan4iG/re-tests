import lackey
from re_tests_plugin import *
import firebird.driver as fdb


def test_check_role_public(lock_employee, open_connection):
    with fdb.connect("employee") as con:
        con.execute_immediate("""
CREATE OR ALTER FUNCTION NEW_FUNC
RETURNS VARCHAR(5)
AS
begin
  RETURN 'five';
end
""")
        con.execute_immediate("CREATE OR ALTER PACKAGE NEW_PACK AS BEGIN END;")
        con.execute_immediate("RECREATE PACKAGE BODY NEW_PACK AS BEGIN END;")
        con.commit()
    lackey.rightClick("icon_conn_open.png")
    lackey.click("tree_reload_menu.png")
    lackey.click("tools.png")
    lackey.click("tab_grant_manager.png")
    results = []
    results.append(lackey.exists("text_PUBLIC.png"))
    
    list_b = list(lackey.findAll("button_down.png"))
    b = max(list_b, key=lambda i: i.getTarget().getY())
    b = b.getTarget()

    for _ in range(6):
        lackey.click(b)
        lackey.type("{DOWN}")
        results.append(lackey.exists("text_PUBLIC.png"))

    lackey.click("icon_cross.png")
    
    if results[1] != None:
        results[1] = True
    assert results == [None, True, None, None, None, None, None]