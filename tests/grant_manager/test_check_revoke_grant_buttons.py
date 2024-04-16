import lackey
from re_tests_plugin import *

def click_top_button(image):
    list_b = list(lackey.findAll(image))
    b = min(list_b, key=lambda i: i.getTarget().getY())
    return b.getTarget()

def test_check_revoke_grant_buttons():
    pass
    # NEED FULL REWORK!!!

    # lackey.click("tools.png")
    # lackey.click("tab_grant_manager.png")
    # lackey.click("text_Users.png")
    # lackey.click("text_Roles.png")
    # lackey.click("text_PUBLIC.png")
    # lackey.click("text_Execute.png")
    # lackey.SettingsMaster.MinSimilarity = 0.9999
    # lackey.click(click_top_button("bt_revoke_column.png"))
    # lackey.click(click_top_button("bt_revoke_row.png"))
    # result1 = len(list(lackey.findAll("red_grant_status.png")))
    # lackey.click("bt_revoke_all.png")
    # lackey.SettingsMaster.MinSimilarity = 0.97
    # lackey.click(click_top_button("bt_revoke_row.png"))
    # lackey.click(click_top_button("bt_grant_column.png"))
    # lackey.click(click_top_button("bt_revoke_row.png"))
    # lackey.click(click_top_button("bt_grant_row.png"))
    # lackey.SettingsMaster.MinSimilarity = 0.9999
    # result2 = len(list(lackey.findAll("red_grant_status.png")))
    # lackey.SettingsMaster.MinSimilarity = 0.97
    # lackey.click("bt_grant_all.png")
    # lackey.click(click_top_button("bt_grant_option_column.png"))
    # lackey.click(click_top_button("bt_grant_option_row.png"))
    # lackey.SettingsMaster.MinSimilarity = 0.9999
    # result3 = len(list(lackey.findAll("red_grant_status.png")))
    # lackey.SettingsMaster.MinSimilarity = 0.97
    # lackey.click("bt_grant_option_all.png")
    # lackey.click("text_Usage.png")
    # lackey.click(click_top_button("bt_revoke_column.png"))
    # lackey.click("icon_cross.png")  
    # assert 50 < result1 >= 5 
    # assert result2 >= 50
    # assert result3 == 0