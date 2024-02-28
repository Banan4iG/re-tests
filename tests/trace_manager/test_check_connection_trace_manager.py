import lackey, os
from re_tests_plugin import *

conf_path = os.environ.get('TEMP') + "/" + "test_conf.conf"
log_path = os.environ.get('TEMP') + "/" + "test_log.fbtrace_text"

def test_1(open_connection):
    lackey.click("tools.png")
    lackey.click("trace_manager.png")
    
    #conf file creation
    lackey.click("bt_buildconfigurationfile.png")
    lackey.click(lackey.exists("server_version.png").getTarget().right(50))
    lackey.click("reddatabase_3.0.png")
    array_of_bars = list(lackey.findAll("empty_bar.png"))
    lackey.click(array_of_bars[8])
    lackey.App.setClipboard(conf_path)
    lackey.type("v",lackey.Key.CTRL)
    lackey.click("save.png")
    result1 = lackey.exists("bt_OK_blue.png")
    lackey.click("bt_OK_blue.png")
    lackey.type("{ESC}")

    #create connection
    lackey.click(lackey.exists("text_connections.png").getTarget().right(300))
    mouse = lackey.Mouse()
    lackey.click(mouse.getPos().below(40))
    lackey.click("NONE.png")
    lackey.click(lackey.exists("NONE.png").getTarget().below(40))
    bts = list(lackey.findAll("bt_more.png"))
    lackey.click(bts[1])
    lackey.type("a",lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE) 
    lackey.App.setClipboard(conf_path)
    lackey.type("v",lackey.Key.CTRL)
    lackey.type("{ENTER}")
    lackey.click("log_to_file.png")
    lackey.type("{TAB}{TAB}")
    lackey.App.setClipboard(log_path)
    lackey.type("v",lackey.Key.CTRL)
    lackey.click("start.png")

    #fill log file
    lackey.click("session_manager.png")
    lackey.click("refresh.png")
    lackey.click("icon_visible_columns.png")
    lackey.click("table_a_lot_left.png")
    lackey.click("table_runner.png")
    time.sleep(1)
    lackey.wheel(lackey.Mouse.WHEEL_DOWN, 1)
    lackey.click("event_type.png")
    lackey.click("table_right.png")
    lackey.click("table_runner.png")
    lackey.wheel(lackey.Mouse.WHEEL_DOWN, 15)
    lackey.click("username.png")
    lackey.click("table_right.png")
    lackey.click("type_query_service.png")
    lackey.click("table_right.png")
    lackey.click("type_query_service.png")
    lackey.click("table_up.png")
    lackey.type("{ESC}")
    lackey.click("system_audit.png")
    array_of_stops = list(lackey.findAll("stop.png"))
    lackey.click(array_of_stops[0])
    lackey.click(array_of_stops[1])
    lackey.click("tab_trace_manager_grid_view.png")
    lackey.click("clear_table.png")
    result1 = lackey.exists("clear_table_result.png")
    lackey.rightClick("tab_trace_manager_blue.png")
    lackey.click("bt_tab_close_all.png")
    assert result1 != None


def test_2(open_connection):
    lackey.click("tools.png")
    lackey.click("trace_manager.png")
    time.sleep(2)
    bts_open_file = list(lackey.findAll("icon_open_file.png"))
    lackey.click(bts_open_file[1])
    lackey.click("file_name.png")
    lackey.App.setClipboard(log_path)
    lackey.type("v",lackey.Key.CTRL)
    lackey.click("open.png")
    lackey.click(lackey.exists("filter_column.png").getTarget().right(100))
    lackey.click("filter_column_chosen.png")
    lackey.click("table_text.png")
    lackey.type("Start")
    result1 = lackey.exists("table_log_check_highlight_1.png")
    result2 = lackey.exists("table_log_check_highlight_2.png")
    lackey.click("filter_choosing.png")
    lackey.click("filter_chosen.png")
    result3 = lackey.exists("table_log_check_filter.png")
    lackey.rightClick("tab_trace_manager_blue.png")
    lackey.click("bt_tab_close_all.png")
    assert result1 != None
    assert result2 != None
    assert result3 != None

if os.path.exists(conf_path): os.remove(conf_path)
if os.path.exists(log_path): os.remove(log_path)

