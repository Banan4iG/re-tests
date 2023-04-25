import lackey
from re_tests_plugin import *

def test_1(open_connection):
    move_location = lackey.find("icon_connected.png").getTarget()
    mouse = lackey.Mouse()
    mouse.move(loc=move_location)
    time.sleep(1)
    result = lackey.find("hint_disconnect.png")
    assert result != None

def test_2():
    move_location = lackey.find("icon_disconnected.png").getTarget()
    mouse = lackey.Mouse()
    mouse.move(loc=move_location)
    time.sleep(1)
    result = lackey.find("hint_connect.png")
    assert result != None
