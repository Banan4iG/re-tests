import lackey
from re_tests_plugin import *
import firebird.driver as fdb


def check_user(number):
    lackey.rightClick("tree_user_name" + str(number) + ".png")
    lackey.click("tree_edit_menu.png")
    lackey.click("tab_ddl_to_create.png")
    result = lackey.exists("sql_text_user" + str(number) + ".png")
    lackey.click("bt_OK.png")
    return result

def test_1(open_connection):
    with fdb.connect(database='localhost:employee', user=ADMIN_NAME, password=ADMIN_PASSWORD) as con:
        cur = con.cursor()
        cur.execute('CREATE USER "DEMO" PASSWORD \'pass\'')
        cur.execute('CREATE USER "dEmO" PASSWORD \'pass\'')
        con.commit()
        cur.close()
    
    lackey.click("tree_plus.png")
    lackey.rightClick("icon_users.png")
    lackey.click("tree_reload_menu.png")
    all_plus = lackey.findAll("tree_plus.png")
    lackey.click(list(all_plus)[8])
    result1 = check_user(1)
    result2 = check_user(2)

    with fdb.connect(database='localhost:employee', user=ADMIN_NAME, password=ADMIN_PASSWORD) as con:
        cur = con.cursor()
        cur.execute('DROP USER "DEMO"')
        cur.execute('DROP USER "dEmO"')
        con.commit()
        cur.close()

    assert result1 != None
    assert result2 != None