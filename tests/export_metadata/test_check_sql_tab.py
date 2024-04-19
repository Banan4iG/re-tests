import lackey
import firebird.driver as fdb
from subprocess import Popen, PIPE
from re_tests_plugin import * 
from . import *
import keyboard


def start(rdb5: bool):
	create_objects(rdb5)
	list_con = list(lackey.findAll("icon_conn.png"))
	for i in list_con:
		lackey.doubleClick(i)
		time.sleep(2)
	list_b = list(lackey.findAll("icon_conn_open.png"))
	b = min(list_b, key=lambda i: i.getTarget().getY())
	lackey.rightClick(b.getTarget())
	lackey.click("tree_export_metadata_menu.png")
	lackey.click("bt_extract.png")
	count = 0
	while (count != 5):
		if lackey.exists("icon_massage.png") != None:
			break
		count += 1
		time.sleep(5)
	lackey.click("bt_OK_blue.png")
	time.sleep(0.5)

def finish(rdb5: bool):
	delete_objects(rdb5)
	lackey.rightClick("tab_compare_db_blue.png")
	lackey.click("bt_tab_close_all.png")
	lackey.doubleClick("icon_disconnect_all.png")
	
	list_b = list(lackey.findAll("icon_conn.png"))
	b = max(list_b, key=lambda i: i.getTarget().getY())
	lackey.rightClick(b.getTarget())
	lackey.click("tree_remove_conn.png")
	lackey.type("{ENTER}")

def delete_files(files: list):
	for file in files:
		if os.path.exists(file):
			os.remove(file)

def create_connect(test_base_path: str):
	lackey.App.setClipboard(test_base_path)
	keyboard.press('ctrl')
	lackey.type('n', lackey.Key.SHIFT)
	keyboard.release('ctrl')
	time.sleep(2)
	lackey.type("{TAB}"*6)
	lackey.type("v", lackey.Key.CTRL)
	lackey.type("{TAB}"*8)
	lackey.type("sysdba{TAB}masterkey")

def compare_db(test_base_path: str):
	lackey.click("tools.png")
	lackey.click("compare_db.png")
	list_b = list(lackey.findAll("button_down.png"))
	b = max(list_b, key=lambda i: i.getTarget().getY())
	lackey.click(b.getTarget())	
	lackey.type("{DOWN}{ENTER}")
	list_b = list(lackey.findAll("bt_select_all.png"))
	b = min(list_b, key=lambda i: i.getTarget().getX())
	lackey.click(b.getTarget())
	lackey.click("bt_compare.png")
	count = 0
	while (count != 5):
		if lackey.exists("icon_massage.png") != None:
			break
		count += 1
		time.sleep(5)
	lackey.SettingsMaster.MinSimilarity = 0.99
	result = lackey.exists("compare_result.png")
	lackey.SettingsMaster.MinSimilarity = 0.97
	lackey.click("bt_OK_blue.png")
	return result

def test_save_script(lock_employee):
	vars = Variables()
	ver = vars.get_version
	srv_ver = vars.get_srv_version
	home = vars.home_directory
	rdb5 = True if (ver == "5.0" and srv_ver == "RedDatabase") else False 
	start(rdb5)
	lackey.click("tab_SQL.png")
	lackey.click("bt_save_script.png")

	script_path = os.environ.get('TEMP') + "\\script.sql"
	test_base_path = os.environ.get('TEMP') + "\\test.fdb"
	ts_path = os.environ.get('TEMP') + "\\file.ts"
	
	files = [script_path, test_base_path, ts_path]

	delete_files(files)

	lackey.App.setClipboard(script_path)
	lackey.type("a", lackey.Key.CTRL)
	lackey.type("v", lackey.Key.CTRL)
	lackey.click("bt_save_script_b.png")
	time.sleep(2)
	with open(script_path, "r") as file:
		context = file.read()
	context = context.replace("employee.fdb", test_base_path).replace(f"{home}examples\\empbuild\\file.ts", ts_path)
	with open(script_path, "w") as file:
		file.write(context)
	
	con = fdb.create_database(test_base_path)
	con.close()

	print(home)
	subprocess.call(f"{home}\isql -q -i \"{script_path}\"")

	create_connect(test_base_path)
	result = compare_db(test_base_path)
		
	finish(rdb5)

	delete_files(files)

	assert result != None

def test_execute_script(lock_employee):
	vars = Variables()
	ver = vars.get_version
	srv_ver = vars.get_srv_version
	home = vars.home_directory
	rdb5 = True if (ver == "5.0" and srv_ver == "RedDatabase") else False 
	test_base_path = os.environ.get('TEMP') + "\\test.fdb"
	ts_path = os.environ.get('TEMP') + "\\file.ts"
	files = [test_base_path, ts_path]
	delete_files(files)
	con = fdb.create_database(test_base_path)
	con.close()
	create_connect(test_base_path)
	
	start(rdb5)
	lackey.click("tab_SQL.png")
	lackey.click("bt_execute_script.png")
	time.sleep(2)
	lackey.click("button_down.png")
	list_b = list(lackey.findAll("text_new_connection_1.png"))
	b = max(list_b, key=lambda i: i.getTarget().getX())
	lackey.click(b.getTarget())

	# No supported yet. See RS-173096 (https://tracker.red-soft.ru/issues/173096)
	# lackey.type("f", lackey.Key.CTRL)
	# lackey.type("a", lackey.Key.CTRL)
	# lackey.App.setClipboard(f"{home}examples\\empbuild\\file.ts")
	# lackey.type("v", lackey.Key.CTRL)
	# lackey.type("{TAB}{SPACE}{TAB}")
	# lackey.App.setClipboard(ts_path)
	# lackey.type("a", lackey.Key.CTRL)
	
	# lackey.type("v", lackey.Key.CTRL)
	# lackey.click("bt_replace_all.png")
	# lackey.type("{ESC}")
	
	list_b = list(lackey.findAll("icon_execute_script.png"))
	b = max(list_b, key=lambda i: i.getTarget().getY())
	lackey.click(b.getTarget())

	time.sleep(10)

	result = compare_db(test_base_path)

	finish(rdb5)

	delete_files(files)

	assert result != None