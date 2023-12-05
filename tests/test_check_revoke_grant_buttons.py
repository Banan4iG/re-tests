import lackey
from re_tests_plugin import *

def test_check_revoke_grant_buttons(open_connection):
    lackey.click("tools.png")
    lackey.click("tab_grant_manager.png")
    lackey.click("text_PUBLIC.png")
    result = lackey.exists("text_revoke_grant_visible.png")
    lackey.click("bt_revoke_column.png")
    lackey.click("bt_revoke_row.png")
    lackey.click("bt_revoke_all.png")
    lackey.click("bt_grant_column.png")
    lackey.click("bt_grant_row.png")
    lackey.click("bt_grant_all.png")
    lackey.click("bt_grant_option_column.png")
    lackey.click("bt_grant_option_row.png")
    lackey.click("bt_grant_option_all.png")
    lackey.click("bt_refresh.png")
    lackey.click("text_Usage.png")
    lackey.click("bt_revoke_column.png")
    lackey.click("icon_cross.png")
    assert result != None