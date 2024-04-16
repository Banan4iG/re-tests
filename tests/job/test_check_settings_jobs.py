import lackey
from re_tests_plugin import *


vars = Variables()
ver = vars.get_version
srv_ver = vars.get_srv_version

@pytest.mark.skipif((not (ver == "5.0" and srv_ver == "RedDatabase")), reason="Not supported")
def test_settings(open_connection):
    lackey.click("tree_plus.png")
    lackey.rightClick("icon_jobs.png")
    lackey.click("tree_create_menu.png")
    lackey.type("{TAB}")
    lackey.type("a",lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE) 
    lackey.type("Newjob0")

    #start and end checking
    array_of_buttons_more = list(lackey.findAll("bt_calendar.png"))
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
    lackey.click((array_of_buttons_up_down[0]).getTarget().above(5)) 
    lackey.click(array_of_buttons_more[0])
    lackey.click("button_a_lot_right.png")
    lackey.click("button_left.png")
    lackey.click("settings_starting_chosen.png")
    lackey.click((array_of_buttons_up_down[1]).getTarget().left(30))
    lackey.type("a",lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE) 
    lackey.type("25:00:00.000")
    lackey.click("PSQL.png")
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