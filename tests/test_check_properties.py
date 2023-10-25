import lackey
from re_tests_plugin import *


def test_1(open_connection):
    lackey.click("icon_conns.png")
    lackey.SettingsMaster.MinSimilarity = 0.8
    lackey.rightClick("icon_disconnected_db_browser.png")
    lackey.SettingsMaster.MinSimilarity = 0.97
    lackey.click("properties.png")
    result = lackey.exists("bt_test.png")
    lackey.rightClick("tab_db_browser.png")
    lackey.click("bt_tab_close_all.png")
    assert result != None