import lackey
from re_tests_plugin import *

def test_check_in_query_editor(open_connection):
    lackey.click("tab_query_editor.png")
    lackey.click("tab_query_editor_text.png")
    lackey.type("emplo{ENTER}{ENTER}")
    lackey.type("   employee {ENTER}")
    lackey.type(lackey.Key.BACKSPACE, lackey.Key.CTRL)
    lackey.type("select * from emplo{ENTER}{ENTER}")
    result = lackey.exists("text_highlight_obj.png")
    lackey.type("a", lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE)
    assert result != None