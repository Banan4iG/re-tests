import lackey
from re_tests_plugin import *

check_dict = {}

def every_checking(time):
    check_dict[time] = [0, 1, 2]
    lackey.click(time + "_every_tick.png")
    check_dict[time][0] = lackey.exists(time + "_every_tick_checking.png")
    lackey.click("every.png")
    lackey.click("every_block_tickes.png")
    lackey.click("every_block_tickes_chosen.png")
    lackey.click("starting.png")
    name = "zero" if (time == "min" or time == "hour") else time
    lackey.click(name + "_every_block_choosing.png")
    lackey.click(name + "_every_block_starting_chosen.png")
    lackey.click("ending.png")
    lackey.click(name + "_every_block_choosing.png")
    lackey.click(name + "_every_block_ending_chosen.png")
    check_dict[time][1] = lackey.exists(time + "_every_checking.png")
    lackey.click("every_tick_between.png")
    array = list(lackey.findAll(name + "_every_block_choosing.png"))
    lackey.click(array[0])
    lackey.click(name + "_every_tick_between_block_starting_chosen.png")
    lackey.click(array[1])
    lackey.click(name + "_every_tick_between_block_ending_chosen.png")
    check_dict[time][2] = lackey.exists(time + "_every_tick_between_checking.png")


def test_cron_false(open_connection):
    lackey.click("tree_plus.png")
    lackey.rightClick("icon_jobs.png")
    lackey.click("tree_create_menu.png")
    lackey.click("extra_jobs_comment.png")
    lackey.type("begin /*job is here*/ end")
    lackey.click("jobs_schedule.png")
    lackey.click(lackey.exists("jobs_cron.png").getTarget().right(100))
    lackey.type("a",lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE) 
    lackey.type("59 23 41 21 34")
    lackey.click("jobs_advanced.png")
    result1 = lackey.exists("jobs_cron_checking_min.png")
    lackey.click("jobs_hours.png")
    result2 = lackey.exists("jobs_cron_checking_hour.png")
    lackey.click("jobs_days.png")
    result3 = lackey.exists("jobs_cron_checking_day_false.png")
    lackey.click("jobs_cron_checking_day_false.png")
    lackey.click("jobs_cron_checking_day_true.png")
    lackey.click("jobs_months.png")
    result4 = lackey.exists("jobs_cron_checking_mon_false.png")
    lackey.click("jobs_cron_checking_mon_false.png")
    lackey.click("jobs_cron_checking_mon_true.png")
    lackey.click("jobs_weekdays.png")
    result5 = lackey.exists("jobs_cron_checking_weekday_false.png")
    lackey.click("jobs_cron_checking_weekday_false.png")
    lackey.click("jobs_cron_checking_weekday_true.png")
    lackey.click("bt_OK.png")
    result6 = lackey.exists("jobs_cron_false_result.png")
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


def test_cron_true(open_connection):
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
    lackey.click("jobs_advanced.png")
    result1 = lackey.exists("jobs_cron_checking_min.png")
    every_checking("min")
    lackey.click("jobs_hours.png")
    result2 = lackey.exists("jobs_cron_checking_hour.png")
    every_checking("hour")
    lackey.click("jobs_days.png")
    result3 = lackey.exists("jobs_cron_checking_day.png")
    every_checking("day")
    lackey.click("jobs_months.png")
    result4 = lackey.exists("jobs_cron_checking_mon.png")
    #every_checking("mon")
    lackey.click("jobs_weekdays.png")
    result5 = lackey.exists("jobs_cron_checking_weekday.png")
    #every_checking("weekday")
    lackey.click("bt_OK.png")
    result6 = lackey.exists("test_jobs_cron_true_result.png")
    #result6 = lackey.exists("jobs_cron_true_result.png")
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
    for time in check_dict:
        for i in time:
            assert i != None
