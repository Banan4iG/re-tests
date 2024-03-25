import pytest
import lackey
import time
import platform
import os
import subprocess
from firebird.driver import driver_config
from firebird.driver import connect_server
from firebird.driver import SrvInfoCode, DirectoryCode


driver_config.server_defaults.host.value = 'localhost'
driver_config.server_defaults.user.value = 'SYSDBA'
driver_config.server_defaults.password.value = 'masterkey'


with connect_server(server='localhost') as srv:
    home_directory = srv.info.home_directory
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
        time.sleep(7)
    return pid

def pytest_exception_interact(report):
    if report.failed:
        lackey.App.close("Red Expert")
        home_dir = os.path.expanduser("~")
        history_file = os.path.join(home_dir,'.redexpert/202301/ConnectionHistory.xml')
        if os.path.exists(history_file):
            os.remove(history_file)
        open_app()

@pytest.fixture
def open_connection():
    #actions befor test:
    lackey.App.focus("Red Expert")
    lackey.doubleClick("icon_conn.png")
    time.sleep(2)    #waiting time to open connection
    lackey.click("icon_conn_open.png")
    #actions after test:
    yield
    if lackey.exists("icon_conn_open.png"):
        lackey.doubleClick("icon_conn_open.png")

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