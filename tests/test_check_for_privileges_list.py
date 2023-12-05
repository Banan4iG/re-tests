import lackey
from re_tests_plugin import *

def test_check_for_privileges_list(open_connection):
    lackey.click("tools.png")
    lackey.click("tab_grant_manager.png")
    lackey.click("text_Users.png")
    result = lackey.exists("text_privileges_visible.png")
    lackey.click("text_Roles.png")
    lackey.click("text_Roles.png")
    lackey.click("text_Views.png")
    lackey.click("text_Views.png")
    lackey.click("text_Triggers.png")
    lackey.click("text_Triggers.png")
    lackey.click("text_Procedures.png")
    lackey.click("text_Procedures.png")
    lackey.click("text_Functions.png")
    lackey.click("text_Functions.png")
    lackey.click("text_Packages.png")
    lackey.click("text_Packages.png")
    lackey.click("text_Users.png")
    lackey.click("icon_cross.png")
    assert result != None