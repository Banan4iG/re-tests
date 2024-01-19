import lackey
from re_tests_plugin import *

def test_check_checkbox(open_connection):
    lackey.click("tools.png")
    lackey.click("tab_grant_manager.png")
    lackey.click("checkbox_Show_empty.png")
    result1 = len(list(lackey.findAll("icon_system_tables.png")))
    lackey.click("table_runner.png")
    lackey.wheel(lackey.Mouse.WHEEL_DOWN, 30)
    result2 = len(list(lackey.findAll("icon_system_packages.png")))
    result3 = len(list(lackey.findAll("icon_system_sequences.png")))
    lackey.click("icon_cross.png")
    assert result1 > 0
    if version == "3.0":
        assert result2 == 0
    else:
        assert result2 > 0
    assert result3 > 0