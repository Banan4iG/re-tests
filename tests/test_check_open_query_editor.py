import lackey
import os
from re_tests_plugin import *
from pathlib import Path

def test_empty_saved():
    lackey.doubleClick("icon_conn.png")
    time.sleep(2)
    result1 = lackey.exists("tab_query_editor_text.png")
    lackey.doubleClick("icon_conn_open.png")

    lackey.doubleClick("icon_conn.png")
    time.sleep(2)
    result2 = lackey.exists("tab_query_editor_text.png")
    lackey.doubleClick("icon_conn_open.png")

    assert result1 != None
    assert result2 != None

def test_empty():
    home_dir = os.path.expanduser("~")
    for path in Path(os.path.join(home_dir,'.redexpert/202301/QueryEditor')).glob("script*.sql"):
        os.remove(path)
    
    lackey.doubleClick("icon_conn.png")
    time.sleep(2)
    result1 = lackey.exists("tab_query_editor_text.png")
    lackey.doubleClick("icon_conn_open.png")

    lackey.doubleClick("icon_conn.png")
    time.sleep(2)
    result2 = lackey.exists("tab_query_editor_text.png")
    lackey.doubleClick("icon_conn_open.png")

    lackey.type("s", lackey.Key.CTRL)

    assert result1 != None
    assert result2 != None

def test_saved():
    lackey.doubleClick("icon_conn.png")
    time.sleep(2)
    lackey.App.setClipboard("select * from employee;")
    lackey.type("v", lackey.Key.CTRL)
    lackey.doubleClick("icon_conn_open.png")

    lackey.doubleClick("icon_conn.png")
    time.sleep(2)
    result1 = lackey.exists("text_query_1.png")
    lackey.doubleClick("icon_conn_open.png")

    lackey.doubleClick("icon_conn.png")
    time.sleep(2)
    result2 = lackey.exists("text_query_1.png")
    lackey.type("a", lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE)
    lackey.doubleClick("icon_conn_open.png")

    assert result1 != None
    assert result2 != None