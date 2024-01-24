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
    lackey.click("icon_visible_columns.png")
    lackey.click("bt_dbl_triangle_left.png")
    bt = lackey.exists("bt_dbl_triangle_right.png")
    lackey.click(bt) 
    (_, middle_y) = bt.getTarget().getTuple()
    (x, y) = lackey.exists("selected_columns.png").getTarget().getTuple()
    max_y = y+((middle_y-y)*2)
    for _ in range(5):
        current_y = random.randint(y+5, max_y)
        lackey.click(lackey.Location(x, current_y))
        lackey.click(random.choice(avaible_actions))
        lackey.click("table_runner.png")
        lackey.wheel(lackey.Mouse.WHEEL_DOWN, 10)
        current_y = random.randint(y+5, max_y)
        lackey.click(lackey.Location(x, current_y))
        lackey.click(random.choice(avaible_actions))
        lackey.click("table_runner.png")
        lackey.wheel(lackey.Mouse.WHEEL_UP, 10)
  
    lackey.click("bt_dbl_triangle_left.png")

    results = []
    for i in range(1, 6):
        count = 0
        while lackey.exists(f"sorted_available_columns{i}.png") == None:
            lackey.click("table_runner.png")
            lackey.wheel(lackey.Mouse.WHEEL_DOWN, 1)
            count += 1
            if count == 5:
                break
        results.append(lackey.exists(f"sorted_available_columns{i}.png"))
    lackey.type("{ESC}")
    lackey.SettingsMaster.MinSimilarity = 0.93        
    lackey.rightClick("tab_trace_manager_blue.png")
    lackey.SettingsMaster.MinSimilarity = 0.97
    lackey.click("bt_tab_close_all.png")
    assert results != [None, None, None, None]