import lackey, os
from re_tests_plugin import *

conf_path = os.environ.get('TEMP') + "/" + "test_conf.conf"
check_dict = {}
def array_filling():    
    check_dict["format"] = ["0", "0"]
    check_dict["enabled"] = ["true", "true"]
    check_dict["log_security_incidents"] = ["true", "false"]
    check_dict["log_initfini"] = ["true", "false"]
    check_dict["log_connections"] = ["true", "false"]
    check_dict["log_transactions"] = ["true", "false"]
    check_dict["log_statement_prepare"] = ["true", "false"]
    check_dict["log_statement_free"] = ["true", "false"]
    check_dict["log_statement_start"] = ["true", "false"]
    check_dict["log_statement_finish"] = ["true", "false"]
    check_dict["log_procedure_start"] = ["true", "false"]
    check_dict["log_procedure_finish"] = ["true", "false"]
    check_dict["log_function_start"] = ["true", "false"]
    check_dict["log_function_finish"] = ["true", "false"]
    check_dict["log_trigger_start"] = ["true", "false"]
    check_dict["log_service_query"] = ["true", "false"]
    check_dict["log_trigger_finish"] = ["false", "true"]
    check_dict["log_context"] = ["false", "true"]
    check_dict["log_errors"] = ["false", "true"]
    check_dict["log_warnings"] = ["false", "true"]
    check_dict["print_plan"] = ["false", "true"]
    check_dict["print_perf"] = ["false", "true"]
    check_dict["log_blr_requests"] = ["false", "true"]
    check_dict["print_blr"] = ["false", "true"]
    check_dict["log_dyn_requests"] = ["false", "true"]
    check_dict["print_dyn"] = ["false", "true"]
    check_dict["log_privilege_changes"] = ["false", "true"]
    check_dict["log_changes_only"] = ["false", "true"]
    check_dict["log_services"] = ["false", "true"]
    check_dict["include_user_filter"] = ["ship", "0"]
    check_dict["exclude_user_filter"] = ["819", "0"]
    check_dict["include_process_filter"] = ["14", "0"]
    check_dict["exclude_process_filter"] = ["true", "0"]
    check_dict["include_filter"] = ["0", "ship"]
    check_dict["exclude_filter"] = ["0", "819"]
    check_dict["connection_id"] = ["0", "14"]
    check_dict["log_filename"] = ["0", "true"]
    check_dict["max_log_size"] = ["1024", "0"]
    check_dict["time_threshold"] = ["2048", "0"]
    check_dict["max_sql_length"] = ["4096", "0"]
    check_dict["max_blr_length"] = ["8192", "0"]
    check_dict["max_dyn_length"] = ["0", "1024"]
    check_dict["max_arg_length"] = ["0", "2048"]
    check_dict["max_arg_count"] = ["0", "4096"]

def test_1(open_connection):
    lackey.click("tools.png")
    lackey.click("trace_manager.png")
    time.sleep(3)
    lackey.click("tick.png")
    lackey.click("bt_buildconfigurationfile.png")
    lackey.click(lackey.exists("server_version.png").getTarget().right(50))
    lackey.click("reddatabase_3.0.png")
    array_of_ticks = list(lackey.findAll("tick.png"))
    for i in range(13, 25):
        lackey.click(array_of_ticks[i])
    lackey.click(array_of_ticks[25])
    array_of_bars = list(lackey.findAll("empty_bar.png"))
    lackey.click(array_of_bars[0])
    lackey.type("ship")
    lackey.click(array_of_bars[1])
    lackey.type("819")
    lackey.click(array_of_bars[2])
    lackey.type("14")
    lackey.click(array_of_bars[3])
    lackey.type("true")
    array_of_zero_bars = list(lackey.findAll("zero_bar.png"))
    lackey.click(array_of_zero_bars[0])
    lackey.type("a",lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE) 
    lackey.type("1024")
    lackey.click(array_of_zero_bars[1])
    lackey.type("a",lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE) 
    lackey.type("2048")
    lackey.click(array_of_zero_bars[2])
    lackey.type("a",lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE) 
    lackey.type("4096")
    lackey.click(array_of_zero_bars[3])
    lackey.type("a",lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE) 
    lackey.type("8192")
    array_of_bars = list(lackey.findAll("empty_bar.png"))
    lackey.click(array_of_bars[4])
    lackey.App.setClipboard(conf_path)
    lackey.type("v",lackey.Key.CTRL)
    lackey.click("save.png")
    lackey.click("bt_OK_blue.png")
    lackey.type("{ESC}")
    #file check
    array_filling()
    f = open(conf_path, "r")
    for i in range(3):
        f.readline()
    for i in range(38):
        first, equal, second = list(f.readline().split())
        assert check_dict[first][0] == second
        f.readline()
    for i in range(5):
        f.readline()
    for i in range(9):
        first, equal, second = list(f.readline().split())
        assert check_dict[first][0] == second
        f.readline()
    f.close()
    lackey.rightClick("tab_trace_manager.png")
    lackey.click("bt_tab_close_all.png")

def test_2(open_connection):
    lackey.click("tools.png")
    lackey.click("trace_manager.png")
    time.sleep(3)
    lackey.click("tick.png")
    lackey.click("bt_buildconfigurationfile.png")
    lackey.click(lackey.exists("server_version.png").getTarget().right(50))
    lackey.click("reddatabase_3.0.png")
    array_of_ticks = list(lackey.findAll("tick.png"))
    for i in range(0, 13):
        lackey.click(array_of_ticks[i])
    lackey.click(array_of_ticks[26])
    array_of_bars = list(lackey.findAll("empty_bar.png"))
    lackey.click(array_of_bars[4])
    lackey.type("ship")
    lackey.click(array_of_bars[5])
    lackey.type("819")
    lackey.click(array_of_bars[6])
    lackey.type("14")
    lackey.click(array_of_bars[7])
    lackey.type("true")
    array_of_bars = list(lackey.findAll("zero_bar.png"))
    lackey.click(array_of_bars[4])
    lackey.type("a",lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE) 
    lackey.type("1024")
    lackey.click(array_of_bars[5])
    lackey.type("a",lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE) 
    lackey.type("2048")
    lackey.click(array_of_bars[6])
    lackey.type("a",lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE) 
    lackey.type("4096")
    array_of_bars = list(lackey.findAll("empty_bar.png"))
    lackey.click(array_of_bars[4])
    lackey.App.setClipboard(conf_path)
    lackey.type("v",lackey.Key.CTRL)
    lackey.click("save.png")
    lackey.click("bt_OK_blue.png")
    lackey.type("{ESC}")

    #file check
    array_filling()
    f = open(conf_path, "r")
    for i in range(3):
        f.readline()
    for i in range(38):
        first, equal, second = list(f.readline().split())
        assert check_dict[first][1] == second
        f.readline()
    for i in range(5):
        f.readline()
    for i in range(9):
        first, equal, second = list(f.readline().split())
        assert check_dict[first][1] == second
        f.readline()
    f.close()
    lackey.rightClick("tab_trace_manager.png")
    lackey.click("bt_tab_close_all.png")

if os.path.exists(conf_path): 
    os.remove(conf_path)