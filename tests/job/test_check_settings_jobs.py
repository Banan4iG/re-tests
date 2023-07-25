import lackey
from re_tests_plugin import *

def test_settings(open_connection):
    lackey.click("tree_plus.png")
    lackey.rightClick("icon_jobs.png")
    lackey.click("tree_create_menu.png")
    lackey.click(lackey.exists("Name.png").getTarget().right(100))
    lackey.type("a",lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE) 
    lackey.type("New_job_0")

    #start and end checking
    array_of_buttons_more = list(lackey.findAll("button_more.png"))
    lackey.click((array_of_buttons_more[0]).getTarget().left(50))
    lackey.type("July 6, 2024")
    lackey.click((array_of_buttons_more[1]).getTarget().left(50))
    lackey.type("July 6, 2023")
    array_of_buttons_up_down = list(lackey.findAll("button_up_down.png"))
    lackey.click((array_of_buttons_up_down[0]).getTarget().left(30))
    lackey.type("a",lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE) 
    lackey.type("12:00:00.000")
    lackey.click((array_of_buttons_up_down[0]).getTarget().above(5))
    lackey.click((array_of_buttons_up_down[0]).getTarget().above(5)) #pressing the button does not work the first time, as it requires resetting from the fill line
    array_of_NULL = list(lackey.findAll("NULL.png"))
    lackey.click(array_of_NULL[0])
    lackey.click(array_of_buttons_more[0])
    lackey.click("button_a_lot_right.png")
    lackey.click("button_left.png")
    lackey.click("settings_starting_chosen.png")
    lackey.click((array_of_buttons_up_down[1]).getTarget().left(30))
    lackey.type("a",lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE) 
    lackey.type("25:00:00.000")
    array_of_buttons_down = list(lackey.findAll("button_down.png"))
    lackey.click(array_of_buttons_down[1])
    lackey.click("BASH.png")
    lackey.click("Active.png")
    lackey.click("jobs_schedule.png")
    lackey.click(lackey.exists("jobs_cron.png").getTarget().right(100))
    lackey.type("a",lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE) 
    lackey.type("59 23 11 2 3")

    #final
    lackey.click("bt_OK.png")
    result1 = lackey.exists("settings_final.png")
    result2 = len(list(lackey.findAll("text_success.png")))
    lackey.click("bt_rollback.png")
    lackey.click("bt_cancel.png")
    lackey.click("bt_YES.png")
    assert result1 != None
    assert result2 >= 1