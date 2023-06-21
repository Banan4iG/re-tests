import lackey
from re_tests_plugin import *

def test_1(open_connection):
    lackey.click("icon_query_editor.png")
    lackey.type("alter trigger fts$trig_22 sql  security definer ")
    lackey.click("icon_execute_query.png")
    result1 = lackey.exists("test_NULL_Trigger.png")
    assert result1 != None
