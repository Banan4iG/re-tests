import lackey
from re_tests_plugin import *

def test_check_profiler_connection(open_connection):
    lackey.click("tools.png")
    lackey.click("text_profiler.png")
    lackey.click("text_New.png")
    result1 = lackey.exists("text_New_blue.png")
    lackey.click("text_New.png")
    lackey.click("text_127.png")
    result2 = lackey.exists("text_127_blue.png")
    lackey.click("text_127.png")
    lackey.click("icon_cross.png")
    assert result1 != None
    assert result2 != None