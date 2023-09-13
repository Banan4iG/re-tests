import lackey
from re_tests_plugin import *

def test_1():
    for _ in range(3):
        lackey.click("tools.png")
        lackey.click("trace_manager.png")

    lackey.rightClick("tab_trace_manager_blue.png")
    lackey.click("bt_tab_close_all.png")
    result1 = lackey.exists("tab_trace_manager_blue.png")
    result2 = lackey.exists("tab_trace_manager.png") 
    assert result1 == None
    assert result2 == None