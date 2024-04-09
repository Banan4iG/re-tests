import lackey
from re_tests_plugin import * 
from . import *

def init_extract() -> bool:
	rdb5 = True if (version == "5.0" and srv_version == "RedDatabase") else False 
	create_objects(rdb5)
	lackey.doubleClick("icon_conn.png")
	time.sleep(2)
	list_b = list(lackey.findAll("icon_conn_open.png"))
	b = min(list_b, key=lambda i: i.getTarget().getY())
	lackey.rightClick(b.getTarget())
	lackey.click("tree_export_metadata_menu.png")
	return rdb5

def check_ignore(script: str) -> list:
	result = [
		script.count("COMMENT ON"),
		script.count("COMPUTED FIELDs defining"),
		script.count("PRIMARY KEYs defining"),
		script.count("FOREIGN KEYs defining"),
		script.count("UNIQUE KEYs defining"),
		script.count("CHECK KEYs defining"),
		]
	return result

def extract():
	lackey.click("bt_extract.png")
	while lackey.exists("icon_massage.png") == None:
		time.sleep(1)
	lackey.click("bt_OK_blue.png")
	time.sleep(0.5)

	lackey.click("tab_SQL.png")
	mouse = lackey.Mouse()
	lackey.click(mouse.getPos().below(100))

	lackey.type('a', lackey.Key.CTRL)
	lackey.type('c', lackey.Key.CTRL)

def finish(rdb5: bool):
	delete_objects(rdb5)
	lackey.rightClick("tab_export_metadata_blue.png")
	lackey.click("bt_tab_close_all.png")
	lackey.doubleClick("icon_conn_open.png")

def test_check_no_ignore():
	rdb5 = init_extract()
	extract()
	script_without_properties = lackey.App.getClipboard()

	result = check_ignore(script_without_properties)
	
	finish(rdb5)

	assert result == [16, 1, 1, 1, 1, 1]


def test_check_ignore():
	rdb5 = init_extract()
	
	list_b = list(lackey.findAll("bt_select_all.png"))
	b = max(list_b, key=lambda i: i.getTarget().getX())
	lackey.click(b.getTarget())
	extract()
	script_with_properties = lackey.App.getClipboard()

	result = check_ignore(script_with_properties)

	finish(rdb5)

	assert result == [0, 0, 0, 0, 0, 0]



