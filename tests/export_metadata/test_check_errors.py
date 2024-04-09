import lackey
from re_tests_plugin import * 


def test_1(open_connection):
	lackey.rightClick("icon_conn_open.png")
	lackey.click("tree_export_metadata_menu.png")
	list_b = list(lackey.findAll("bt_select_all.png"))
	b = min(list_b, key=lambda i: i.getTarget().getX())
	lackey.click(b.getTarget())
	lackey.click("bt_extract.png")
	result1 = lackey.exists("icon_warning.png")
	lackey.click("bt_OK_blue.png")
	lackey.click("tab_SQL.png")
	lackey.click("bt_save_script.png")
	result2 = lackey.exists("icon_warning.png")
	lackey.click("bt_OK_blue.png")
	lackey.click("bt_execute_script.png")
	result3 = lackey.exists("icon_warning.png")
	lackey.click("bt_OK_blue.png")
	lackey.rightClick("tab_db_metadata_blue.png")
	lackey.click("bt_tab_close_all.png")
	assert result1 != None	
	assert result2 != None
	assert result3 != None