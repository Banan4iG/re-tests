import lackey
from re_tests_plugin import *
import random

avaible_actions = (
    "bt_sngl_triangle_up.png",
    "bt_sngl_triangle_down.png",
    "bt_dbl_triangle_up.png",
    "bt_dbl_triangle_down.png"
)


def test_1():
    lackey.click("tools.png")
    lackey.click("trace_manager.png")
    lackey.click("visible_columns.png")
    lackey.click("bt_dbl_triangle_left.png")
    lackey.click("bt_dbl_triangle_right.png")    

    x = 1450
    for i in range(5):
        y = random.randint(205, 950)
        lackey.click(lackey.Location(x, y))
        lackey.click(random.choice(avaible_actions))
        lackey.click("table_runner.png")
        lackey.wheel(lackey.Mouse.WHEEL_DOWN, 6)
        y = random.randint(205, 950)
        lackey.click(lackey.Location(x, y))
        lackey.click(random.choice(avaible_actions))
        lackey.click("table_runner.png")
        lackey.wheel(lackey.Mouse.WHEEL_UP, 6)
  
    lackey.click("bt_dbl_triangle_left.png")
    result1 = lackey.exists("sorted_available_columns1.png")
    result2 = lackey.exists("sorted_available_columns2.png") 
    lackey.click("table_runner.png")
    lackey.wheel(lackey.Mouse.WHEEL_DOWN, 6)
    result3 = lackey.exists("sorted_available_columns3.png")
    result4 = lackey.exists("sorted_available_columns4.png")
    lackey.rightClick("tab_trace_manager_blue.png")
    lackey.click("bt_tab_close_all.png")
    assert result1 != None
    assert result2 != None
    assert result3 != None
    assert result4 != None