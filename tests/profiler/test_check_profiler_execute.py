import lackey
from re_tests_plugin import *

def test_check_profiler_execute(open_connection):
    lackey.click("tab_query_editor_text.png")
    lackey.type("SELECT * FROM JOB")
    lackey.click("icon_profiler_execute.png")
    result1 = lackey.exists("icon_profiler_select.png")
    lackey.click("discard.png")
    lackey.click("icon_cross.png")
    lackey.type("a", lackey.Key.CTRL)
    lackey.type("{BACKSPACE}")
    assert result1 != None