import lackey
from re_tests_plugin import *

def test_check_display_list(open_connection):
    lackey.click("tools.png")
    lackey.click("tab_grant_manager.png")
    lackey.click("text_Display_All.png")
    result = lackey.exists("text_display_list_visible.png")
    lackey.click("text_Granted_Only.png")
    lackey.click("text_Granted_Only.png")
    lackey.click("text_Non_Granted_Only.png")
    lackey.click("text_Non_Granted_Only.png")
    lackey.click("text_Display_All.png")
    lackey.click("icon_cross.png")
    assert result != None