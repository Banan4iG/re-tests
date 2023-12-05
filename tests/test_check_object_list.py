import lackey
from re_tests_plugin import *

def test_check_object_list(open_connection):
    lackey.click("tools.png")
    lackey.click("tab_grant_manager.png")
    lackey.click("text_Tables.png")
    result = lackey.exists("text_object_list_visible.png")
    lackey.click("checkbox_Tables.png")
    lackey.click("checkbox_Global.png")
    lackey.click("checkbox_Views.png")
    lackey.click("checkbox_Procedures.png")
    lackey.click("checkbox_Functions.png")
    lackey.click("checkbox_Packages.png")
    lackey.click("checkbox_Sequences.png")
    lackey.click("checkbox_Exceptions.png")
    lackey.click("checkbox_Tables.png")
    lackey.click("checkbox_Global.png")
    lackey.click("checkbox_Views.png")
    lackey.click("checkbox_Procedures.png")
    lackey.click("checkbox_Functions.png")
    lackey.click("checkbox_Packages.png")
    lackey.click("checkbox_Sequences.png")
    lackey.click("checkbox_Exceptions.png")
    lackey.click("icon_cross.png")
    assert result != None