import lackey
from re_tests_plugin import *

def test_check_profiler_checkboxes(open_connection):
    lackey.click("tools.png")
    lackey.click("text_profiler.png")
    lackey.click("text_Default_view.png")
    result1 = lackey.exists("text_Default_checkbox.png")
    lackey.click("text_Extended_view.png")
    result2 = lackey.exists("text_Extended_checkbox.png")
    lackey.click("text_Compact_view.png")
    lackey.click("text_Round_Values.png")
    result3 = lackey.exists("text_Round_checkbox.png")
    lackey.click("text_Round_Values.png")
    lackey.click("icon_cross.png")
    assert result1 != None
    assert result2 != None
    assert result3 != None