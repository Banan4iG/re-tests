from unittest import result

import lackey
from re_tests_plugin import *

def test_check_refresh_button(open_connection):
    lackey.click("tools.png")
    lackey.click("tab_user_manager.png")
    result = lackey.exists("text_refresh_button_visible.png")
    lackey.click("refresh.png")
    lackey.click("icon_cross.png")
    assert result != None