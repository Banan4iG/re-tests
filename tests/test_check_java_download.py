import lackey
from re_tests_plugin import *
import time
import os
from pathlib import Path
import shutil
import winreg
import subprocess


#@pytest.mark.skip(reason="This test no work yet")
def test_1():
    #prepare
    lackey.App.close("Red Expert")
    time.sleep(2)
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

    home_dir = os.path.expanduser("~")
    for path in Path(os.path.join(home_dir,'.redexpert')).glob(".cache_java_path*"):
        os.remove(path)
    
    JAVA_HOME = os.environ.get('JAVA_HOME')
    if JAVA_HOME:
        os.environ.pop('JAVA_HOME', None)

    java_list = list()

    java_keys = [r'SOFTWARE\JavaSoft\JDK', r'SOFTWARE\JavaSoft\Java Development Kit', r'SOFTWARE\IBM\Java Development Kit', r'SOFTWARE\JavaSoft\Java Runtime Environment']
    for java_key in java_keys:
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, java_key) as key:
                i = 0
                while True:
                    try:
                        subkey_name = winreg.EnumKey(key, i)
                        subkey = winreg.OpenKey(key, subkey_name)
                        java_path = winreg.QueryValueEx(subkey, "JavaHome")[0]
                        new_java_path = java_path[:java_path.find("Java")+4]
                        java_list.append(new_java_path)
                        i += 1
                    except OSError:
                        break
        except:
            continue
    
    java_list.append("C:\\Program Files (x86)\\Java")
    list(set(java_list))
    for java in java_list:
        if os.path.isdir(java):
            new_java = java.replace("Java", "Java_b")
            os.rename(java, new_java)

    # lackey.App.open(path_to_exe)
    subprocess.Popen(['powershell', f"start-process '{path_to_exe}'"])
    time.sleep(15)
    
    #test
    lackey.click("rb_download_java_auto.png")
    lackey.click("bt_ok_java.png")

    while(not lackey.exists("icon_conn.png")):
        time.sleep(1)
    result = lackey.exists("icon_conn.png")

    lackey.App.close("Red Expert")

    # finish
    time.sleep(2)
    for path in Path(os.path.join(home_dir,'.redexpert')).glob("java*"):
        shutil.rmtree(path, ignore_errors = True)

    for java in java_list:
        old_java = java.replace("Java", "Java_b")
        if os.path.isdir(old_java):
            os.rename(old_java, java)
    
    if JAVA_HOME:
        os.environ['JAVA_HOME'] = JAVA_HOME

    # lackey.App.open(path_to_exe)
    subprocess.Popen(['powershell', f"start-process '{path_to_exe}'"])
    time.sleep(7)
    assert result != None
