import lackey
from re_tests_plugin import *

def test_check_profiler_buttons(open_connection):
    lackey.click("tools.png")
    lackey.click("text_profiler.png")
    lackey.click("start.png")
    result1 = lackey.exists("transparent_start.png")
    lackey.click("pause.png")
    lackey.click("bt_OK_blue.png")
    result2 = lackey.exists("transparent_pause.png")
    lackey.click("resume.png")
    result3 = lackey.exists("transparent_resume.png")
    lackey.click("stop.png")
    lackey.click("bt_OK_blue.png")
    result4 = lackey.exists("transparent_stop.png")
    lackey.click("start.png")
    lackey.click("bt_cancel.png")
    lackey.click("discard.png")
    lackey.click("icon_cross.png")
    assert result1 != None
    assert result2 != None
    assert result3 != None
    assert result4 != None