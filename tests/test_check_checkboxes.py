import lackey
from re_tests_plugin import *

def test_check_checkboxes(open_connection):
    lackey.click("tools.png")
    lackey.click("tab_grant_manager.png")
    lackey.click("checkbox_Show_empty.png")
    lackey.click("checkbox_Invert_Filter_empty.png")
    result1 = lackey.exists("checkbox_Show.png")
    result2 = lackey.exists("checkbox_Invert_Filter.png")
    lackey.click("checkbox_Invert_Filter.png")
    lackey.click("checkbox_Show.png")
    lackey.click("icon_cross.png")
    assert result1 != None
    assert result2 != None