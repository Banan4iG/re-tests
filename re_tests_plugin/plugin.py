import pytest
import lackey
import time
import platform
import os
import subprocess
from firebird.driver import driver_config
from firebird.driver import connect_server
from firebird.driver import SrvInfoCode


driver_config.server_defaults.host.value = 'localhost'
driver_config.server_defaults.user.value = 'SYSDBA'
driver_config.server_defaults.password.value = 'masterkey'


with connect_server(server='localhost') as srv:
    for ver in ["3.0", "5.0"]:
        index = srv.info.version.find(ver)
        if index > -1:
            version = ver
            break
    
    for srv_ver in ["Firebird", "RedDatabase"]:
        index = srv.info.get_info(SrvInfoCode.SERVER_VERSION).find(srv_ver)
        if index > -1:
            srv_version = srv_ver
            break

    print(version, srv_version)

def plus_find(name_of_the_group):
    return lackey.exists(name_of_the_group).getTarget().left(25)


def open_app():
    pid = lackey.App("Red Expert").getPID()
    if pid == -1:
        DIST = os.environ.get('DIST')
        ARCH = os.environ.get('ARCH')
        if DIST:
            path_to_exe = DIST + "\\bin"
            if ARCH == "x86_64":
                path_to_exe += "\\RedExpert64.exe" 
            else:
                path_to_exe += "\\RedExpert.exe"
        else:
            path_to_exe = '"C:\\Program Files\\RedExpert\\bin\\RedExpert64.exe"'
        
        subprocess.Popen(['powershell', f"start-process '{path_to_exe}'"])
        time.sleep(5)
    return pid


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
    if tests_failed_after == tests_failed_before:
        lackey.doubleClick("icon_conn_open.png")
    else:
        lackey.App.close("Red Expert")
        home_dir = os.path.expanduser("~")
        os.remove(os.path.join(home_dir,'.redexpert/202301/ConnectionHistory.xml'))
        open_app()
        
        # bt_cancel = lackey.exists("bt_cancel.png")
        # if bt_cancel != None:
        #     lackey.click(bt_cancel)
        #     bt_yes = lackey.exists("bt_YES.png")
        #     if bt_yes != None:
        #         lackey.click(bt_yes)
        # bt_close = lackey.exists("bt_close.png")
        # if bt_close != None:
        #     lackey.click(bt_close)
        
    
    # if tests_failed_after > tests_failed_before:
    #     bt_ok = lackey.exists("bt_OK_blue.png")
    #     if bt_ok != None:
    #         lackey.click(bt_ok)

@pytest.fixture(scope='session', autouse=True)
def init_test_session(): 
    pid = open_app()
    lackey.App.focus("Red Expert")
    image_path = ["files/images/"]

    #code for the future
    # if platform.system() == "Windows":
    #     image_path += ["Windows/"]
    # else:
    #     image_path += ["Linux/"]
    
    lackey.SettingsMaster.ImagePaths = image_path
    lackey.SettingsMaster.MinSimilarity = 0.97
    lackey.SettingsMaster.MoveMouseDelay = 0
    yield
    if pid == -1:
        lackey.App.close("Red Expert")