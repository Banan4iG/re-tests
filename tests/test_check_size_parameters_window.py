import lackey
from re_tests_plugin import *
import time


def test_1(open_connection):
    lackey.click("tab_query_editor.png")
    lackey.click("tab_query_editor_text.png")
    lackey.type("select cast(:test as integer) from rdb$database")
    lackey.click("icon_execute_query.png")
    start = lackey.exists("ms_text_input_parameters_start.png")
    x_start = start.getTopLeft().getX()
    end = lackey.exists("ms_text_input_parameters_end.png")
    x_end = end.getTopRight().getX()
    print(x_end-x_start)
    lackey.type("123456")
    result = lackey.exists("ms_input_parameters_with_int.png")
    lackey.click("bt_cancel.png")
    time.sleep(1)
    lackey.type("a", lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE)
    assert x_end-x_start >= 200
    assert result != None