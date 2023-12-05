import lackey
from re_tests_plugin import *

def test_check_filter(open_connection):
    lackey.click("tools.png")
    lackey.click("tab_grant_manager.png")
    lackey.click("filter_empty.png")
    lackey.type("t")
    result = lackey.exists("text_filter_visible.png")
    lackey.click("text_filter_visible.png")
    lackey.type("{BACKSPACE}")
    lackey.click("icon_cross.png")
    assert result != None