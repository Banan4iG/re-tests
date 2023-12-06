import lackey
from re_tests_plugin import *

def test_check_object_list(open_connection):
    lackey.click("tools.png")
    lackey.click("tab_grant_manager.png")
    lackey.click("text_Tables.png")
    result1 = lackey.exists("text_object_list_visible.png")
    lackey.click("checkbox_Tables.png")
    lackey.click("user_SYSDBA_blue.png")
    result2 = lackey.exists("text_checkbox_Tables_visible.png")
    lackey.click("text_Global_Views.png")
    lackey.click("checkbox_Global.png")
    lackey.click("user_SYSDBA_blue.png")
    lackey.click("text_Views_Procedures.png")
    lackey.click("checkbox_Views.png")
    lackey.click("user_SYSDBA_blue.png")
    result3 = lackey.exists("text_checkbox_Views_visible.png")
    lackey.click("text_Procedures_Functions.png")
    lackey.click("checkbox_Procedures.png")
    lackey.click("user_SYSDBA_blue.png")
    result4 = lackey.exists("text_checkbox_Procedures_visible.png")
    lackey.click("text_Functions_Packages.png")
    lackey.click("checkbox_Functions.png")
    lackey.click("user_SYSDBA_blue.png")
    lackey.click("text_Packages_Sequences.png")
    lackey.click("checkbox_Packages.png")
    lackey.click("user_SYSDBA_blue.png")
    lackey.click("text_Sequences_Exceptions.png")
    lackey.click("checkbox_Sequences.png")
    lackey.click("user_SYSDBA_blue.png")
    result5 = lackey.exists("text_checkbox_Sequences_visible.png")
    lackey.click("text_Exceptions_Empty.png")
    lackey.click("checkbox_Exceptions.png")
    lackey.click("user_SYSDBA_blue.png")
    result6 = lackey.exists("text_checkbox_Exceptions_visible.png")
    lackey.click("text_Empty.png")
    lackey.click("checkbox_Tables.png")
    lackey.click("checkbox_Global.png")
    lackey.click("checkbox_Views.png")
    lackey.click("checkbox_Procedures.png")
    lackey.click("checkbox_Functions.png")
    lackey.click("checkbox_Packages.png")
    lackey.click("checkbox_Sequences.png")
    lackey.click("checkbox_Exceptions.png")
    lackey.click("icon_cross.png")
    assert result1 != None
    assert result2 != None
    assert result3 != None
    assert result4 != None
    assert result5 != None
    assert result6 != None