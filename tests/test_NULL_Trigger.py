import lackey
from re_tests_plugin import *

def test_1(open_connection):
    lackey.click("tab_query_editor_text.png")
    lackey.type("alter trigger fts$trig_22 sql  security definer ")
    lackey.click("icon_execute_query.png")
    lackey.click("closing_the_query_editor.png")
    result1 = lackey.exists("test_NULL_Trigger.png")
    assert result1 != None
