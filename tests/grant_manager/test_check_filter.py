import lackey
from re_tests_plugin import *

def test_check_filter(open_connection):
    lackey.click("tools.png")
    lackey.click("tab_grant_manager.png")
    lackey.click("filter_empty.png")
    lackey.type("CUSTOMER")
    result1 = lackey.exists("text_filter_visible.png")
    time.sleep(1)
    result2 = lackey.exists("text_object_filter_visible.png")
    lackey.click("checkbox_Invert_Filter_empty.png")
    result3 = lackey.exists("text_invert_filter_visible.png")
    lackey.click("icon_cross.png")
    assert result1 != None
    assert result2 != None
    assert result3 != None