import lackey
from re_tests_plugin import *

def test_check_display_list(open_connection):
    lackey.click("tools.png")
    lackey.click("tab_grant_manager.png")
    lackey.click("text_Users.png")
    lackey.click("text_Roles.png")
    lackey.click("text_PUBLIC.png")
    lackey.click("text_Display_All.png")
    result1 = lackey.exists("text_display_list_visible.png")
    lackey.click("text_Granted_Only.png")
    lackey.click("text_Granted_Only.png")
    result2 = lackey.exists("text_Granted_Only_visible.png")
    lackey.click("text_Non_Granted_Only.png")
    lackey.click("text_Non_Granted_Only.png")
    result3 = lackey.exists("text_Non_Granted_Only_visible.png")
    lackey.click("text_Display_All.png")
    lackey.click("icon_cross.png")
    assert result1 != None
    assert result2 != None
    assert result3 != None