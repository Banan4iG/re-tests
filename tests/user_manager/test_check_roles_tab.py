import lackey
from re_tests_plugin import *
import firebird.driver as fdb


def test_check_roles_tab(open_connection):
    lackey.click("tools.png")
    lackey.click("tab_user_manager.png")
    lackey.click("tab_roles.png")
    lackey.click("bt_add.png")
    lackey.type("{TAB}")
    lackey.type("a", lackey.Key.CTRL)
    lackey.type("test_role")
    lackey.click("bt_OK.png")
    lackey.click("bt_commit.png")
    result1 = lackey.exists("text_TEST_ROLE.png")
    with fdb.connect("employee") as con:
        cur = con.cursor()
        cur.execute("select CAST(rdb$role_name as VARCHAR(10)) from rdb$roles where rdb$role_name='TEST_ROLE';")
        result2 = cur.fetchone()
        cur.close()
    lackey.click("text_TEST_ROLE.png")
    lackey.click("tree_delete_menu.png")
    lackey.click("bt_commit.png")
    lackey.rightClick("tab_user_manager_blue.png")
    lackey.click("bt_tab_close.png")
    assert result1 != None
    assert result2 == ('TEST_ROLE ',)