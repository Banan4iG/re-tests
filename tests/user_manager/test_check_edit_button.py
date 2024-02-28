import lackey
from re_tests_plugin import *
import firebird.driver as fdb


def test_check_edit_button(open_connection):
    with fdb.connect("employee") as con:
        con.execute_immediate("CREATE USER TEST_USER PASSWORD 'pass';")
        con.commit()
    lackey.click("tools.png")
    lackey.click("tab_user_manager.png")
    lackey.click("text_TEST_USER.png")
    lackey.click("tree_edit_menu.png")
    lackey.click(lackey.exists("text_first_name.png").getTarget().right(100))
    lackey.type("first{TAB}middle{TAB}last{TAB}{SPACE}{TAB}{SPACE}")
    lackey.click("tab_comment.png")
    mouse = lackey.Mouse()
    lackey.click(mouse.getPos().offset(30, 100))
    lackey.type("description")
    lackey.click("bt_OK.png")
    lackey.click("bt_commit.png")
    with fdb.connect("employee") as con:
        cur = con.cursor()
        cur.execute("""select cast(sec$user_name as VARCHAR(9)), 
sec$first_name, 
sec$middle_name,
sec$last_name, 
sec$active, 
sec$admin, 
sec$description,
cast(sec$plugin as VARCHAR(3))  from sec$users where sec$user_name='TEST_USER';""")
        result = cur.fetchone()
        cur.close()
    lackey.rightClick("tab_user_manager_blue.png")
    lackey.click("bt_tab_close.png")
    with fdb.connect("employee") as con:
        con.execute_immediate("DROP USER TEST_USER;")
        con.commit()
    assert result == ('TEST_USER', 'first', 'middle', 'last', False, True, 'description', 'Srp')