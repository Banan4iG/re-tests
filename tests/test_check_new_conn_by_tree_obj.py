import lackey
import keyboard
from re_tests_plugin import *

def create_new_conn():
    keyboard.press('ctrl')
    lackey.type('n', lackey.Key.SHIFT)
    keyboard.release('ctrl')
    time.slep(2)
    lackey.type("{TAB}"*6)
    lackey.type("employee.fdb")
    lackey.type("{TAB}"*8)
    lackey.type("sysdba{TAB}masterkey")

def remove_conn():
    lackey.doubleClick("icon_conn_open.png")
    list_b = list(lackey.findAll("icon_conn.png"))
    b = max(list_b, key=lambda i: i.getTarget().getY())
    lackey.rightClick(b.getTarget())
    lackey.click("tree_remove_conn.png")
    lackey.type("{ENTER}")
    lackey.rightClick("icon_abstract_object.png")
    lackey.click("bt_tab_close_all.png")

def test_1():
    create_new_conn()
    list_b = list(lackey.findAll("icon_conn.png"))
    b = max(list_b, key=lambda i: i.getTarget().getY())
    lackey.rightClick(b.getTarget())	
    lackey.click("tree_connect.png")
    result = lackey.exists("icon_conn_open.png") 
    remove_conn()
    assert result != None

def test_2():
    create_new_conn()
    list_b = list(lackey.findAll("icon_conn.png"))
    b = max(list_b, key=lambda i: i.getTarget().getY())
    lackey.doubleClick(b.getTarget())
    result = lackey.exists("icon_conn_open.png") 
    remove_conn()
    assert result != None