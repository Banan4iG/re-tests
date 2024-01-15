import lackey
from re_tests_plugin import *

def find_grants():
    return len(list(lackey.findAll("icon_grant_with.png"))), len(list(lackey.findAll("icon_no_grant.png"))) 
                      

def test_check_display_list(open_connection):
    lackey.click("tools.png")
    lackey.click("tab_grant_manager.png")
    lackey.click("text_Users.png")
    lackey.click("text_Roles.png")
    lackey.click("text_PUBLIC.png")
    lackey.click("table_runner.png")
    lackey.wheel(lackey.Mouse.WHEEL_DOWN, 10)
    grant_with1, no_grant1 = find_grants()
    lackey.click("text_Display_All.png")
    lackey.click("text_Granted_Only.png")
    grant_with2, no_grant2 = find_grants()
    lackey.click("text_Granted_Only.png")
    lackey.click("text_Non_Granted_Only.png")
    grant_with3, no_grant3 = find_grants()
    lackey.click("icon_cross.png")
    assert grant_with1 > 0
    assert no_grant1 > 0

    assert grant_with2 > 0
    assert no_grant2 == 0

    assert grant_with3 == 0
    assert no_grant3 > 0