import pytest
import lackey
import time
import platform

def plus_find(name_of_the_group):
    return lackey.exists(name_of_the_group).getTarget().left(25)

ADMIN_NAME = 'sysdba'
ADMIN_PASSWORD = 'masterkey'

@pytest.fixture
def open_connection(request):
    #actions befor test:
    lackey.App.focus("Red Expert")
    lackey.doubleClick("icon_conn.png")
    time.sleep(2)    #waiting time to open connection
    lackey.click("icon_conn_open.png")
    #actions after test:
    tests_failed_before = request.session.testsfailed
    yield
    tests_failed_after = request.session.testsfailed
    if tests_failed_after > tests_failed_before:
        bt_cancel = lackey.exists("bt_cancel.png")
        if bt_cancel != None:
            lackey.click(bt_cancel)
            bt_yes = lackey.exists("bt_YES.png")
            if bt_yes != None:
                lackey.click(bt_yes)
    lackey.doubleClick("icon_conn_open.png")

@pytest.fixture(scope='session', autouse=True)
def create_connection():
    lackey.App.focus("Red Expert")
    
    image_path = ["files/images/"]

    #code for the future
    # if platform.system() == "Windows":
    #     image_path += ["Windows/"]
    # else:
    #     image_path += ["Linux/"]
    
    lackey.SettingsMaster.ImagePaths = image_path
    lackey.SettingsMaster.MinSimilarity = 0.97
