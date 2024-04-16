import pytest
import lackey
import time
import platform
import os
import subprocess
import shutil
from firebird.driver import driver_config
from firebird.driver import connect_server
from firebird.driver import SrvInfoCode, DirectoryCode


class Variables:
    def __init__(self):
        self.home_directory = home_directory
        self.version = version
        self.srv_version = srv_version
    
    @property
    def get_home(self):
        return self.home_directory
    
    @property
    def get_version(self):
        return self.version
    
    @property
    def get_srv_version(self):
        return self.srv_version


home_directory = ""
version = ""
srv_version = ""

def pytest_configure():
    global home_directory
    global version
    global srv_version

    driver_config.server_defaults.host.value = 'localhost'
    driver_config.server_defaults.user.value = 'SYSDBA'
    driver_config.server_defaults.password.value = 'masterkey'
    
    with connect_server(server='localhost', user='SYSDBA', password='masterkey') as srv:
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
        saved_conn_file = os.path.join(home_dir,'.redexpert/202301/savedconnections.xml')
        if os.path.exists(saved_conn_file):
            with open(saved_conn_file, 'r') as f:
                context = f.read()
            
            if "</connection>" in context:
                context = context[:context.find("</connection>")] + "</connection>\n\n</savedconnections>"
            
                with open(saved_conn_file, 'w') as f:
                    f.write(context)

        if os.path.exists(history_file):
            os.remove(history_file)
        
        open_app()

@pytest.fixture()
def lock_employee():
    subprocess.run([f"{home_directory}nbackup.exe", "-L", f"{home_directory}examples/empbuild/employee.fdb", "-u", "SYSDBA", "-p", "masterkey"])
    time.sleep(1)
    yield
    time.sleep(2)
    delta_file = home_directory + "examples/empbuild/employee.fdb.delta"
    if os.path.exists(delta_file): 
        os.remove(delta_file)
    subprocess.run([f"{home_directory}nbackup.exe", "-F", f"{home_directory}examples/empbuild/employee.fdb"])
    ts_file = home_directory + "examples/empbuild/file.ts"
    if os.path.exists(ts_file):
        os.remove(ts_file)
    
@pytest.fixture()
def copy_employee():
    os.replace(f"{home_directory}examples/empbuild/employee.fdb", f"{home_directory}examples/empbuild/employee_b.fdb")
    time.sleep(1)
    shutil.copy(f"{home_directory}examples/empbuild/employee_b.fdb", f"{home_directory}examples/empbuild/employee.fdb")
    time.sleep(1)
    yield
    copy_file = home_directory + "examples/empbuild/employee.fdb"
    if os.path.exists(copy_file): 
        os.remove(copy_file)
    os.replace(f"{home_directory}examples/empbuild/employee_b.fdb", f"{home_directory}examples/empbuild/employee.fdb")
    ts_file = home_directory + "examples/empbuild/file.ts"
    if os.path.exists(ts_file):
        os.remove(ts_file)

@pytest.fixture()
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