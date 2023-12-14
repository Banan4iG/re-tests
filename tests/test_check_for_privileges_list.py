import lackey
from re_tests_plugin import *

def test_check_for_privileges_list(open_connection):
    lackey.click("tools.png")
    lackey.click("tab_grant_manager.png")
    lackey.click("text_Users.png")
    result1 = lackey.exists("text_privileges_visible.png")
    lackey.click("text_Roles.png")
    result2 = lackey.exists("text_RDB$ADMIN_blue.png")
    lackey.click("text_Roles.png")
    lackey.click("text_Views.png")
    result3 = lackey.exists("text_PHONE_LIST_blue.png")
    lackey.click("text_Views.png")
    lackey.click("text_Triggers.png")
    result4 = lackey.exists("text_Triggers_visible.png")
    lackey.click("text_SAVE_SALARY_CHANGE.png")
    lackey.click("text_SET_CUST_NO.png")
    lackey.click("text_SET_EMP_NO.png")
    lackey.click("text_Triggers.png")
    lackey.click("text_Procedures.png")
    result5 = lackey.exists("text_Procedures_visible.png")
    lackey.click("text_Procedures.png")
    lackey.click("text_Functions.png")
    lackey.click("text_Functions.png")
    lackey.click("text_Packages.png")
    lackey.click("text_Packages.png")
    lackey.click("text_Users.png")
    lackey.click("icon_cross.png")
    assert result1 != None
    assert result2 != None
    assert result3 != None
    assert result4 != None
    assert result5 != None