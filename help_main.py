import os
import sys
#import random
#import datetime
# import string
# import platform
import subprocess
import hashlib
import io
# import linecache
import winreg
import zipfile
import shutil
from win32gui import *
from win32 import win32api
import telnetlib
import time
import requests

class helper_main(object):
    global Program_file,sub_key
    if True == os.path.exists("C:\\Program Files (x86)"):
        Program_file="C:\\Program Files (x86)"
        sub_key=[r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall', r'SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall']
    else:
        Program_file="C:\\Program Files"
        sub_key=[r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall']
    def _exec_cmd(cmd, block=True):
        p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if not block:
            return 0, '', ''
        stdout, stderr = p.communicate() # bytes, bytes
        exit_code = p.returncode # int
        try:
            stdout = bytes.decode(stdout)
        except UnicodeDecodeError:
            try:
                stdout = bytes.decode(stdout, encoding="GBK",errors='ignore')
            except:
                stdout = str(stdout)
        except:
            stdout = str(stdout)
        try:
            stderr = bytes.decode(stderr)
        except UnicodeDecodeError:
            try:
                stderr = bytes.decode(stderr, encoding="GBK",errors='ignore')
            except:
                stderr = str(stderr)
        except:
            stderr = str(stderr)
        return exit_code, stdout, stderr
    def windows_foo():
        titles=set()
        def foo(hwnd,mouse):
            if IsWindow(hwnd) and IsWindowEnabled(hwnd) and IsWindowVisible(hwnd):
                titles.add(GetWindowText(hwnd))
        EnumWindows(foo, 0)
        lt = [t for t in titles if t]
        lt.sort()
        return lt
    def geneMd5(filename):
        m = hashlib.md5()
        file = io.FileIO(filename,'r')
        bytes = file.read(1024)
        while(bytes != b''):
            m.update(bytes)
            bytes = file.read(1024) 
        file.close()
        return m.hexdigest()
    def getFileVersion(file_name):
        info = win32api.GetFileVersionInfo(file_name, os.sep)
        ms = info['FileVersionMS']
        ls = info['FileVersionLS']
        version = '%d.%d.%d.%04d' % (win32api.HIWORD(ms), win32api.LOWORD(ms), win32api.HIWORD(ls), win32api.LOWORD(ls))
        return version
    def compressFolder(folderPath, compressPathName):
        zip = zipfile.ZipFile(compressPathName, 'w', zipfile.ZIP_DEFLATED)
        dict = {}
        for path, dirNames, fileNames in os.walk(folderPath):
            fpath = path.replace(folderPath, '')
            for name in fileNames:
                fullName = os.path.join(path, name)
                name = fpath + '\\' + name
                zip.write(fullName, name)
        zip.close()
        shutil.rmtree(folderPath,True)
    def windows_systeminfo(info_path):
        a,b,c=helper_main._exec_cmd("systeminfo")
        systeminfo_file=open(info_path + "systeminfo.txt","w",encoding='utf8')
        systeminfo_file.write(b)
        systeminfo_file.close()
    def process_module_info(info_path):
        a,b,c=helper_main._exec_cmd("tasklist /v /fo table")
        process_file=open(info_path + "processList.txt","w",encoding='utf8')
        process_file.write(b)
        process_file.close()
        a,b,c=helper_main._exec_cmd("tasklist /m /fo table")
        process_module_file=open(info_path + "processModuleList.txt","w",encoding='utf8')
        process_module_file.write(b)
        process_module_file.close()
    def uem_version_info(info_path):
        uem_version_file=open(info_path + "uem_version.txt","w",encoding='utf8')
        if os.path.isfile(Program_file + "\\Sangfor\\SSL\\UEM\\agent\\SfUemAgent.exe"):
            uem_version=helper_main.getFileVersion(Program_file + "\\Sangfor\\SSL\\UEM\\agent\\SfUemAgent.exe")
            uem_version_file.write("UEMagent的版本号为:"+ uem_version + "\n")
        if os.path.isfile(Program_file + "\\Sangfor\\SSL\\EasyConnect\\aWork.exe"):
            vpn_version=helper_main.getFileVersion(Program_file + "\\Sangfor\\SSL\\EasyConnect\\aWork.exe")
            uem_version_file.write("VPN的版本号为:"+ vpn_version + "\n")
        if os.path.isfile(Program_file + "\\Sangfor\\atrust\\aTrustAgent\aTrustAgent.exe"):
            atrust_version=helper_main.getFileVersion(Program_file + "\\Sangfor\\atrust\\aTrustAgent\aTrustAgent.exe")
            uem_version_file.write("atrust的版本号为:"+ atrust_version + "\n")
        uem_version_file.close()
    def software_info(info_path):
        try:
            software_info_file=open(info_path + "software_info.txt","w",encoding='utf8')
            software_name = []
            print(sub_key)
            for i in sub_key:
                key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, i, 0, winreg.KEY_ALL_ACCESS)
                for j in range(0, (winreg.QueryInfoKey(key)[0])):
                    try:
                        key_name = winreg.EnumKey(key, j)
                        key_path = i + '\\' + key_name
                        #print(key_path)
                        each_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_ALL_ACCESS)
                        DisplayName, REG_SZ = winreg.QueryValueEx(each_key, 'DisplayName')
                        DisplayVersion, REG_SZ = winreg.QueryValueEx(each_key, 'DisplayVersion')
                        DisplayName_Version = DisplayName + "    版本号：" + DisplayVersion
                        #DisplayName = DisplayName.encode('utf-8')
                        software_name.append(DisplayName_Version)
                    except Exception as e:
                        print(str(e))
                        pass
            for i in sub_key:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, i, 0, winreg.KEY_ALL_ACCESS)
                for a in range(0, (winreg.QueryInfoKey(key)[0])):
                    try:
                        key_name = winreg.EnumKey(key, a)
                        key_path = i + '\\' + key_name
                        each_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_ALL_ACCESS)
                        DisplayName, REG_SZ = winreg.QueryValueEx(each_key, 'DisplayName')
                        try:
                            DisplayVersion, REG_SZ = winreg.QueryValueEx(each_key, 'DisplayVersion')
                        except Exception as e:
                            print(str(e))
                            DisplayVersion="版本号为空"
                            pass
                        DisplayName_Version = DisplayName + "    版本号：" + DisplayVersion
                        print(DisplayName_Version)
                        #DisplayName = DisplayName.encode('utf-8')
                        software_name.append(DisplayName_Version)
                    except Exception as e:
                        print(str(e))
                        pass
        except Exception as e:
                    print(str(e))
                    pass
        software_name = list(set(software_name))
        software_name = sorted(software_name)
        for result in software_name:
            software_info_file.write(str(result)+ "\n")
    def dump_log(info_path):
        if os.path.isfile("C:\\Windows\\MEMORY.DMP"):
            helper_main._exec_cmd("copy \"C:\\Windows\\MEMORY.DMP\" " + '"'+ info_path + '"')
            #os.system("copy \"C:\\Windows\\MEMORY.DMP\" " + '"'+ info_path + '"')
        if os.path.exists("C:\\Windows\\Minidump"):
            helper_main._exec_cmd("xcopy \"C:\\Windows\\Minidump\" " + '"'+ info_path + '"' +'/S '+'/Y '+'/I')
    def uem_log(info_path):
        appdata_sangfor = info_path+"\\appdata"
        public_sangfor = info_path+"\\public"
        helper_main._exec_cmd("xcopy \"%appdata%\\Sangfor\\\" "+ '"'+ appdata_sangfor + '"' +'/S '+'/Y '+'/I')
        helper_main._exec_cmd("xcopy \"%public%\\Sangfor\\\" "+ '"'+ public_sangfor + '"' +'/S '+'/Y '+'/I')
    def windows_log(info_path):
        helper_main._exec_cmd("copy \"C:\\Windows\\System32\\winevt\\Logs\\Application.evtx\" " + '"'+ info_path + '"')
        helper_main._exec_cmd("copy \"C:\\Windows\\System32\\winevt\\Logs\\Security.evtx\" " + '"'+ info_path + '"')
        helper_main._exec_cmd("copy \"C:\\Windows\\System32\\winevt\\Logs\\Setup.evtx\" " + '"'+ info_path + '"')
        helper_main._exec_cmd("copy \"C:\\Windows\\System32\\winevt\\Logs\\System.evtx\" " + '"'+ info_path + '"')
    #生成资源文件目录访问路径
    def resource_path(relative_path):
        if getattr(sys, 'frozen', False): #是否Bundle Resource
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)
    #使用资源时调用方式
    # helper_main.resource_path(os.path.join("res","skins\\uem.ico"))
    def telnet_time(addr,telnet_port):
        try:
            time1=time.clock()
            t = telnetlib.Telnet(host=addr, port=telnet_port, timeout=2)
            time2 = time.clock()
            use_time = time2 -time1
            description = addr+":"+str(telnet_port)+"访问时间为"+str(use_time) 
            #print(use_time,description)
        except Exception as e:
            description = addr+":"+str(telnet_port)+"访问"+str(e)
            #这里use_time等于timeout时间
            use_time = 2
            pass
        return use_time, description
    def http_s_time(url):
        try:
            print(url)
            time1=time.clock()
            http_s_get=requests.get(url, verify=False)
            time2 = time.clock()
            use_time = time2 -time1
            response_code = http_s_get.status_code
            print(response_code)
            if response_code == 200:
                response_info = "访问"+url+"成功，耗时："+str(use_time)
            else:
                response_info = "访问"+url+"失败，返回码："+str(response_code)
                use_time = 9.9999
        except Exception as e:
            response_info = "访问"+url+"异常："+str(e)
            use_time = 9.9999
            pass
        return use_time,response_info      
    def filter_log_time(log_type,checkflag,begorend):
        try:
            public_path = os.getenv('PUBLIC')
            appdata_path = os.getenv('APPDATA')
            if log_type == "aTrustCore":
                log_path = appdata_path + "\\Sangfor\\aTrust\\logs\\aTrustAgent_plugins_aTrustCore_h_e.log"
            if log_type == "SfUemClient":
                log_path = public_path + "\\Sangfor\\SSL\\UEM\\Log\\SfUemClient.exe.log"
            if log_type == "explorer":
                log_path = public_path + "\\Sangfor\\SSL\\UEM\\Log\\Explorer.EXE.log"
            if log_type == "Resource OK":
                log_path = appdata_path + "\\Sangfor\\aTrust\\logs\\aTrustAgent_plugins_aTrustCore_h_e.log"
                policy_list=[]
                i=0
                n=0
                statusEvent_login_line=0
                for line in open(log_path,encoding='gbk',errors='ignore'):
                    i = i + 1
                    if "statusEvent|login" in line:
                        statusEvent_login_line = i
                for line1 in open(log_path,encoding='gbk',errors='ignore'):
                    n = n +1
                    if n > statusEvent_login_line:
                        if checkflag in line1 and begorend in line1:
                            policy_list.append(line1)
                log_time = policy_list[0].split(begorend+":")[-1]
                return log_time
            policy_list=[]
            for line in open(log_path,encoding='gbk',errors='ignore'):
                if checkflag in line and begorend in line:
                    policy_list.append(line)
            log_time=policy_list[-1].split(begorend+":")[-1] 
            #print(log_time)
        except Exception as e:
            print(str(e))
            log_time=0
            pass
        #如果取的是end timeStamp 后面还会包含timecost值，需要自行处理
        return log_time  
      

