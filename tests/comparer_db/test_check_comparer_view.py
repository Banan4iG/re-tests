import lackey
from re_tests_plugin import *
from . import create_duplicate_compare, disconnect_delete_duplicate
def test_check_comparer_view(open_connection):
    create_duplicate_compare()
    result1 = lackey.exists("text_Comparing_Finish.png")
    lackey.click("text_View.png")
    lackey.doubleClick("text_To_Create.png")
    result2 = lackey.exists("text_Object_To_Create.png")
    lackey.doubleClick("text_To_Create.png")
    lackey.doubleClick("text_To_Alter.png")
    result3 = lackey.exists("text_Objects_To_Alter.png")
    lackey.doubleClick("text_To_Alter.png")
    lackey.doubleClick("text_To_Drop.png")
    result4 = lackey.exists("text_Objects_To_Drop.png")
    lackey.doubleClick("text_To_Drop.png")
    lackey.click("icon_cross.png")
    disconnect_delete_duplicate()
    assert result1 != None
    assert result2 != None
    assert result3 != None
    assert result4 != None
