import lackey
from re_tests_plugin import *

def test_cron(open_connection):
    lackey.click("tree_plus.png")
    lackey.rightClick("icon_jobs.png")
    lackey.click("tree_create_menu.png")
    lackey.click("extra_jobs_comment.png")
    lackey.type("begin /*job is here*/ end")
    lackey.click("jobs_schedule.png")
    lackey.click(lackey.exists("jobs_cron.png").getTarget().right(100))
    lackey.type("a",lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE) 
    lackey.type("59 23 11 2 3")

    #once a year checking
    lackey.click("once_a_year_left_line.png")
    lackey.type("a",lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE) 
    lackey.type("23:57")
    lackey.click("once_a_year_right_line.png")
    lackey.type("July 7, 2025")
    array_of_buttons_more = list(lackey.findAll("button_more.png"))
    lackey.click(array_of_buttons_more[2])
    lackey.click("button_a_lot_right.png")
    lackey.click("button_left.png")
    lackey.click("once_a_year_right_line_chosen.png")
    result1 = lackey.exists("once_a_year_checking.png")

    #every day checking
    lackey.click("every_day.png")
    lackey.click(lackey.exists("button_up_down.png").getTarget().below(5))
    lackey.click("every_days_choosing.png")
    lackey.type("a",lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE) 
    lackey.type("3")
    result2 = lackey.exists("every_day_checking.png")

    #every week checking
    lackey.click("every_week.png")
    for i in range(2):
        lackey.click(lackey.exists("button_up_down.png").getTarget().above(5))
    lackey.click("every_weeks_choosing.png")
    lackey.type("a",lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE) 
    lackey.type("5")
    lackey.click("button_sunday.png")
    lackey.click("button_friday.png")
    result3 = lackey.exists("every_week_checking.png")

    #every month checking
    lackey.click("every_month.png")
    for i in range(3):
        lackey.click(lackey.exists("button_up_down.png").getTarget().above(5))
    array_of_buttons_down = list(lackey.findAll("button_down.png"))
    lackey.click(array_of_buttons_down[2])
    lackey.click("button_march.png")
    lackey.click("days.png")
    lackey.click(array_of_buttons_down[3])
    lackey.click("every_month_days_chosen.png")
    result4 = lackey.exists("every_month_checking.png")

    #to repeat job every checking
    lackey.click("to_repeat_job_every.png")
    for i in range(2):
        lackey.click(lackey.exists("button_up_down.png").getTarget().below(5))
    array_of_buttons_down = list(lackey.findAll("button_down.png"))
    lackey.click(array_of_buttons_down[4])
    lackey.click("to_repeat_job_every_chosen.png")
    result5 = lackey.exists("to_repeat_job_every_checking.png")

    #final
    lackey.click("bt_OK.png")
    result6 = lackey.exists("cron_jobs_not_advanced_result.png")
    result7 = len(list(lackey.findAll("text_success.png")))
    lackey.click("bt_rollback.png")
    lackey.click("bt_cancel.png")
    lackey.click("bt_YES.png")
    assert result1 != None
    assert result2 != None
    assert result3 != None
    assert result4 != None
    assert result5 != None
    assert result6 != None
    assert result7 >= 1