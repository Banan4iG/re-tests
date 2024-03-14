import lackey
from re_tests_plugin import *
import firebird.driver as fdb
import time


def test_check_refresh_button(open_connection):
    lackey.click("tools.png")
    lackey.click("tab_user_manager.png")
    with fdb.connect("employee") as con:
        con.execute_immediate("CREATE USER TEST_USER PASSWORD 'pass';")
        con.commit()
    result1 = lackey.exists("list_users_sysdba_only.png")
    lackey.click("refresh.png")
    time.sleep(1)
    result2 = lackey.exists("list_users.png")
    with fdb.connect("employee") as con:
        con.execute_immediate("DROP USER TEST_USER;")
        con.commit()
    lackey.rightClick("tab_user_manager_blue.png")
    lackey.click("bt_tab_close.png")
    assert result1 != None
    assert result2 != None