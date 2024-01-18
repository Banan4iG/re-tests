import lackey, os
from re_tests_plugin import *

conf_path = os.environ.get('TEMP') + "/" + "test_conf.conf"
log_path = os.environ.get('TEMP') + "/" + "test_log.fbtrace_text"

@pytest.mark.skipif(srv_version == "Firebird", reason="Not supported")
def test_1(open_connection):
    lackey.click("tools.png")
    lackey.click("trace_manager.png")
    
    #conf file creation
    lackey.click("buildconfigurationfile.png")
    lackey.click(lackey.exists("server_version.png").getTarget().right(50))
    lackey.click("reddatabase_3.0.png")
    lackey.wheel(lackey.Mouse.WHEEL_DOWN, 50)
    lackey.click("just_extra_click.png")
    array_of_bars = list(lackey.findAll("empty_bar.png"))
    lackey.click(array_of_bars[9])
    lackey.type(conf_path)
    lackey.click("save.png")
    result1 = lackey.exists("bt_OK_blue.png")
    lackey.click("bt_OK_blue.png")

    #create connection
    lackey.click("connection.png")
    lackey.click(lackey.exists("buildconfigurationfile.png").getTarget().below(25))
    lackey.click(lackey.exists("buildconfigurationfile.png").getTarget().below(70))
    lackey.click("NONE.png")
    lackey.click(lackey.exists("NONE.png").getTarget().below(40))
    lackey.click("log_to_file.png")
    lackey.click(lackey.exists("without_a_tick_use_config_file.png").getTarget().right(300))
    lackey.type("a",lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE) 
    lackey.type(conf_path)
    lackey.click(lackey.exists("without_a_tick_log_to_file.png").getTarget().right(300))
    lackey.type(log_path)
    lackey.click("start.png")
    lackey.click("buildconfigurationfile.png")

    #fill log file
    lackey.click("session_manager.png")
    lackey.click("refresh.png")
    lackey.click("visible_columns.png")
    lackey.click("table_a_lot_left.png")
    lackey.click("table_runner.png")
    while (lackey.exists("event_type.png") == None and lackey.exists("event_type_blue.png") == None):
        lackey.wheel(lackey.Mouse.WHEEL_DOWN, 6)
    if (lackey.exists("event_type.png")): lackey.click("event_type.png") 
    else: lackey.click("event_type_blue.png")
    lackey.click("table_right.png")


    lackey.click("table_runner.png")
    lackey.wheel(lackey.Mouse.WHEEL_UP, 20)
    while (lackey.exists("username.png") == None and lackey.exists("username_blue.png") == None):
        lackey.wheel(lackey.Mouse.WHEEL_DOWN, 6)
    if (lackey.exists("username.png")): lackey.click("username.png") 
    else: lackey.click("username_blue.png")
    lackey.click("table_right.png")

    lackey.click("table_runner.png")
    lackey.wheel(lackey.Mouse.WHEEL_UP, 20)
    while (lackey.exists("type_query_service.png") == None and lackey.exists("type_query_service_blue.png") == None):
        lackey.wheel(lackey.Mouse.WHEEL_DOWN, 6)
    if (lackey.exists("type_query_service.png")): lackey.click("type_query_service.png") 
    else: lackey.click("type_query_service_blue.png")
    lackey.click("table_right.png")

    lackey.click("type_query_service.png")
    lackey.click("table_up.png")
    lackey.click("session_manager.png")
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


@pytest.mark.skipif(srv_version == "Firebird", reason="Not supported")
def test_2(open_connection):
    lackey.click("tools.png")
    lackey.click("trace_manager.png")
    list_b = list(lackey.findAll("bt_more.png"))
    b = min(list_b, key=lambda i: i.getTarget().getY())
    lackey.click(b.getTarget())
    lackey.click("file_name.png")
    lackey.type(log_path)
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

