import lackey
from re_tests_plugin import *

def test_check_membership_tab(open_connection):
    lackey.click("tools.png")
    lackey.click("tab_user_manager.png")
    lackey.click("tab_membership.png")
    lackey.click("checkbox_empty.png")
    result = lackey.exists("text_membership_tab_visible.png")
    lackey.click("bt_grant_role.png")
    lackey.click("bt_grant_role_with_admin_option.png")
    lackey.click("bt_revoke_role.png")
    lackey.click("checkbox_tick.png")
    lackey.click("icon_cross.png")
    assert result != None