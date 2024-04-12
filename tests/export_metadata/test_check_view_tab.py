import lackey
from re_tests_plugin import * 
import firebird.driver as fdb
import time
from . import create_objects, delete_objects

def count_obj(icon):
	plus = plus_find(icon)
	lackey.click(plus)
	count_objs = len(list(lackey.findAll(icon)))
	lackey.click(plus)
	return count_objs


def test_1():
	rdb5 = True if (version == "5.0" and srv_version == "RedDatabase") else False 
	
	create_objects(rdb5)

	list_obj = ["domains", "tables", "gtt", 
			    "views", "procedures", 
				"functions", "packages", 
				"triggers_for_table", 
				"triggers_for_DDL", "triggers_for_db", 
				"sequences", "exceptions", "UDFs",
				"role", "indices", "collations"]
	
	if rdb5:
		list_obj += ["ts", "jobs"]
	
	lackey.doubleClick("icon_conn.png")
	lackey.rightClick("icon_conn_open.png")
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
	lackey.click("tab_view.png")
	list_b = list(lackey.findAll("tree_plus.png"))
	b = max(list_b, key=lambda i: i.getTarget().getX())
	lackey.click(b.getTarget())

	list_count_obj_actual = []
	for obj in list_obj:
		list_count_obj_actual.append(count_obj(f"icon_{obj}.png"))

	delete_objects(rdb5)

	lackey.rightClick("tab_db_metadata_blue.png")
	lackey.click("bt_tab_close_all.png")
	
	
	list_count_obj_expected = [16, 11, 2, 2, 11, 2, 2, 5, 2, 2, 3, 6, 2, 3, 13, 2]

	if rdb5:
		list_count_obj_expected += [2, 2]

	lackey.doubleClick("icon_conn_open.png")
	assert  list_count_obj_actual == list_count_obj_expected