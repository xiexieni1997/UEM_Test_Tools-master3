# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
from Ui_untitled import Ui_MainWindow 
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import pyqtSignal, QObject, QThread
from xlutils.copy import copy
import xlrd
import xlwt
import hashlib   
import os
import io
import time
from help_main import helper_main 

class mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
    global Program_file
    global uem_agent_list
    global iperf3
    if True == os.path.exists("C:\\Program Files (x86)"):
        Program_file = "C:\\Program Files (x86)"
        uem_agent_list = ["SfUemAgent.exe","UemBaseEngine.dll","UemComCtrl.dll","UemDesktopSpace64.dll","UemDrvComCtrl.dll","UemFileExport.exe","UemRpcPal.dll","UemRpcPal64.dll","UemSDK.dll","UemShellMenu.dll","UemUnifiedHook.dll","UemUnifiedHook64.dll","UemUnifiedPolicy.dll"]    
        iperf3 = helper_main.resource_path(os.path.join("res","exe\\iperf3-win64\\iperf3.exe"))
    else:
        Program_file = "C:\\Program Files"
        uem_agent_list = ["SfUemAgent.exe","UemBaseEngine.dll","UemComCtrl.dll","UemDrvComCtrl.dll","UemFileExport.exe","UemRpcPal.dll","UemSDK.dll","UemShellMenu.dll","UemUnifiedHook.dll","UemUnifiedPolicy.dll"]
        iperf3 = helper_main.resource_path(os.path.join("res","exe\\iperf3-win32\\iperf3.exe"))
    def  __init__ (self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.write_folder)
        self.pushButton_3.clicked.connect(self.start_procexp)
        self.pushButton.clicked.connect(self.read_file)
        self.pushButton_9.clicked.connect(self.read_file_1)
        self.pushButton_4.clicked.connect(self.check_uem_md5)
        self.pushButton_5.clicked.connect(self.check_registry)
        self.pushButton_6.clicked.connect(self.check_service_driver)
        self.pushButton_7.clicked.connect(self.check_version)
        self.pushButton_8.clicked.connect(self.test_app_time)
        self.pushButton_10.clicked.connect(self.check_md5)
        self.pushButton_11.clicked.connect(self.write_folder_1)
        self.pushButton_12.clicked.connect(self.info_collect)
        self.pushButton_13.clicked.connect(self.check_net_policy)
        self.pushButton_14.clicked.connect(self.check_user_policy_service)
        self.pushButton_15.clicked.connect(self.connect_Start)
        self.pushButton_18.clicked.connect(self.connect_Stop)
        self.comboBox_2.currentIndexChanged.connect(self.combox_ip)
        self.comboBox_3.currentIndexChanged.connect(self.combox_port)
        self.pushButton_16.clicked.connect(self.start_ResHacker)
        self.pushButton_17.clicked.connect(self.start_Procmon)
        self.pushButton_19.clicked.connect(self.check_login_time_log)
        self.pushButton_20.clicked.connect(self.check_audit_allip_log)
        self.pushButton_21.clicked.connect(self.check_audit_FileExport_log)
        self.pushButton_22.clicked.connect(self.check_audit_clipboard_log)
        self.pushButton_23.clicked.connect(self.start_hash)
        self.pushButton_24.clicked.connect(self.start_fvie)
        self.pushButton_25.clicked.connect(self.read_file_2)
        self.pushButton_26.clicked.connect(self.collect_app_info)
        self.pushButton_27.clicked.connect(self.save_app_info)
        self.pushButton_28.clicked.connect(self.write_folder_2)
        self.pushButton_29.clicked.connect(self.start_DebugView)
    def read_file(self):
        #选取文件
        filename, filetype =QFileDialog.getOpenFileName(self, "选取文件", "C:/", "All Files(*);;Text Files(*.csv)")
        #print(filename, filetype)
        self.lineEdit.setText(filename)
    def read_file_1(self):
        #选取文件
        filename, filetype =QFileDialog.getOpenFileName(self, "选取文件", "C:/", "All Files(*);;Text Files(*.csv)")
        #print(filename, filetype)
        self.lineEdit_3.setText(filename)
    def read_file_2(self):
        #选取文件
        filename, filetype =QFileDialog.getOpenFileName(self, "选取文件", "C:/", "All Files(*);;Text Files(*.csv)")
        #print(filename, filetype)
        self.lineEdit_9.setText(filename)
    def write_folder(self):
        #选取文件夹
        foldername = QFileDialog.getExistingDirectory(self, "选取文件夹", "C:/")
        #print(foldername)
        self.lineEdit_2.setText(foldername)
    def write_folder_1(self):
        #选取文件夹
        foldername = QFileDialog.getExistingDirectory(self, "选取文件夹", "C:/")
        #print(foldername)
        self.lineEdit_5.setText(foldername)
    def write_folder_2(self):
        #选取文件夹
        foldername = QFileDialog.getExistingDirectory(self, "选取文件夹", "C:/")
        #print(foldername)
        self.lineEdit_14.setText(foldername)
    def check_uem_md5(self):
        try:
            #获取文件路径
            file_path = self.lineEdit.text()
            #获取文件夹路径
            folder_path = self.lineEdit_2.text()
            fail_log = None
            for line in open(file_path):
                path_new = line[:(len(line)-33)].strip().strip('\n')
                #print(path_new[:6] )
                if ( path_new[:6] != "update" ) and ( path_new[:6] != "Sangfo" ):
                    file_path_new = folder_path + '/' + path_new
                    #print(file_path_new)
                    md5_old = line[-33:].strip().strip('\n')
                    m = hashlib.md5()
                    file = io.FileIO(file_path_new,'r')
                    bytes = file.read(1024)
                    while(bytes != b''):
                        m.update(bytes)
                        bytes = file.read(1024) 
                    file.close()
                    md5_new = m.hexdigest()
                    if str(md5_old) == str(md5_new):
                        pass
                    else:
                        fail_log = str(file_path_new + "的MD5值不正确")
                        self.textBrowser_2.append(fail_log)
            if fail_log is None:
                success_result = r'校验成功！'
                self.label_3.setStyleSheet("color:#00ff00")
                self.label_3.setText(success_result)
                self.textBrowser_2.setPlainText('文件MD5校验通过')
            else:
                fail_result = r'校验失败！'
                self.label_3.setStyleSheet("color:#ff0000")
                self.label_3.setText(fail_result)
        except Exception as e:
            fail_result = r'校验异常！'
            self.label_3.setStyleSheet("color:#ff0000")
            self.label_3.setText(fail_result)
            self.textBrowser_2.setPlainText(str(e))
    def check_registry(self):
        try:
            self.textBrowser_2.setPlainText("***检查UEM注册表相关信息是否准确***")
            fail_log = 0
            drivers_iso_list = ["SfUemFesfDt", "SfUemFesfDs", "SfUemFesfIsolate", "SfUemFesfIsolate", "SfUemGuarder"]
            drivers_uem_list = ["SfUemIsoSpace", "SfUemNetIsolate"]
            service_uem_list = ["SfUemAgent"]
            for driver in drivers_iso_list:
                cmd = "reg query HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\services\\" + driver + " /v ImagePath"
                code, stdout, stderr =helper_main._exec_cmd(cmd)
                if str(code) != "0":
                    self.textBrowser_2.append(driver+"驱动注册表键异常")
                    fail_log = fail_log + 1
                else:
                    driver_path = stdout.splitlines()[2].split( )[2]
                    #print(driver_path)
                    if "system32\\Drivers\\" + driver + ".sys" == driver_path:
                        self.textBrowser_2.append(driver+"驱动注册表键值路径ok")
                    else:
                        fail_log = fail_log + 1
                        self.textBrowser_2.append(driver+"驱动注册表键值路径异常")
            for driver_1 in drivers_uem_list:
                cmd = "reg query HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\services\\" + driver_1 + " /v ImagePath"
                code, stdout, stderr =helper_main._exec_cmd(cmd)
                if str(code) != "0":
                    self.textBrowser_2.append(driver_1+"驱动注册表键异常")
                    fail_log = fail_log + 1
                else:
                    driver_1_path = stdout.splitlines()[2].split('    ')[3]
                    #print(driver_1_path)
                    if "\\??\\" + Program_file + "\\Sangfor\\SSL\\UEM\\agent\\Drivers\\" + driver_1 + ".sys" == driver_1_path:
                        self.textBrowser_2.append(driver_1+"驱动注册表键值路径ok")
                    else:
                        self.textBrowser_2.append(driver_1+"驱动注册表键值路径异常")
                        fail_log = fail_log + 1
            for service in service_uem_list:
                cmd = "reg query HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\services\\" + service + " /v ImagePath"
                code, stdout, stderr =helper_main._exec_cmd(cmd)
                if str(code) != "0":
                    self.textBrowser_2.append(service+"服务注册表键异常")
                    fail_log = fail_log + 1
                else:
                    service_path = stdout.splitlines()[2].split('    ')[3]
                    #print(service_path)
                    if '"'+Program_file +'\\Sangfor\\SSL\\UEM\\agent\\' + service + '.exe'+'"' == service_path:
                        self.textBrowser_2.append(service+"服务注册表键值路径ok")
                    else:
                        self.textBrowser_2.append(service+"服务注册表键值路径异常")
                        fail_log = fail_log + 1
            print(fail_log)
            if fail_log == 0:
                success_result = r'UEM注册表信息正确！'
                self.label_4.setStyleSheet("color:#00ff00")
                self.label_4.setText(success_result)
            else:
                fail_result = r'UEM注册表信息异常！'
                self.label_4.setStyleSheet("color:#ff0000")
                self.label_4.setText(fail_result)
        except Exception as e:
            self.textBrowser_2.append(str(e))    
            fail_result = r'UEM注册表信息检查失败！'
            self.label_4.setStyleSheet("color:#ff0000")
            self.label_4.setText(fail_result)    
    def check_service_driver(self):
        try:
            self.textBrowser_2.setPlainText("***检查UEM驱动、服务启动状态***")
            fail_log = 0
            service_driver_list = ["SfUemFesfDt", "SfUemFesfDs", "SfUemFesfIsolate", "SfUemFesfIsolate", "SfUemIsoSpace", "SfUemNetIsolate", "SfUemAgent", "SfUemGuarder"]
            for service_driver in service_driver_list:
                cmd = "sc query " + service_driver 
                code, stdout, stderr =helper_main._exec_cmd(cmd)
                if str(code) != "0":
                    self.textBrowser_2.append(service_driver + "服务未安装")
                    fail_log = fail_log + 1
                else:
                    service_driver_status = stdout.splitlines()[3].split()[3]  
                    #print(service_driver_status)
                    if service_driver_status == "RUNNING":
                        self.textBrowser_2.append(service_driver + "服务运行ok")
                    else:
                        self.textBrowser_2.append(service_driver + "服务状态为：" + service_driver_status)
                        fail_log = fail_log + 1
            #print(fail_log)
            if fail_log == 0:
                success_result = r'UEM服务检查通过！'
                self.label_5.setStyleSheet("color:#00ff00")
                self.label_5.setText(success_result)
            else:
                fail_result = r'UEM服务检查不通过！'
                self.label_5.setStyleSheet("color:#ff0000")
                self.label_5.setText(fail_result)
        except Exception as e:
            self.textBrowser_2.append(str(e))
            fail_result = r'UEM服务检查失败！'
            self.label_5.setStyleSheet("color:#ff0000")
            self.label_5.setText(fail_result)   
    def test_app_time(self):
        try:
            app_path = self.lineEdit_3.text()
            app_name = self.lineEdit_4.text()
            if len(app_name) <= 0 :
                app_name = app_path.split('/')[-1].split('.')[0]
            app_titles = set()
            lt = []
            i = 0
            time1 = time.time()
            os.startfile(app_path)
            while (str(app_name) not in str(lt)) and (i < 20):
                lt = helper_main.windows_foo()
                time.sleep(0.5)
                i = i + 1
                #print(lt)
            time2 = time.time()
            use_time = time2 -time1
            if i < 20:
                self.lcdNumber.display("%.2f" % use_time)
                self.textBrowser.append("打开"+ app_name +"时间为：" + "%.2f" % use_time)
            else:
                self.textBrowser.append("打开"+ app_name + "超过10S")
        except Exception as e:
            self.textBrowser.append("打开程序失败，失败原因：" + str(e))
    def check_md5(self):
        mat = "{:48}\t{:32}"
        try:
            folder_path = self.lineEdit_2.text()
            for fpathe,dirs,fs in os.walk(folder_path):
                for f in fs:
                    full_file = os.path.join(fpathe,f)
                    self.textBrowser_2.append(mat.format(full_file,helper_main.geneMd5(full_file)))
        except Exception as e:
            self.textBrowser_2.append(str(e))
    def info_collect(self):
        try:
            folder_path = self.lineEdit_5.text()
            self.thread1 = QThread()
            self.worker1 = Uem_collect()
            self.worker1.msg_signal.connect(self.collect_flush)
            self.worker1.moveToThread(self.thread1)
            self.thread1.started.connect(lambda:self.worker1.collect_work(folder_path=folder_path))
            self.thread1.start()                 
        except Exception as e:
            self.textBrowser_2.setPlainText(str(e))
    def collect_flush(self,msg):
        self.textBrowser_2.append(str(msg))
        QtWidgets.QApplication.processEvents() 
    def check_version(self):
        try:
            self.textBrowser_2.setPlainText("***检查UEM插件和UEM核心组件版本号***")
            uem_sys_list = ["SfUemGuarder.sys","SfUemIsoSpace.sys","SfUemNetIsolate.sys"]
            for uem_sys in uem_sys_list:
                uem_sys_version=helper_main.getFileVersion(Program_file+"\\Sangfor\\SSL\\UEM\\agent\\Drivers\\"+ uem_sys)
                self.textBrowser_2.append(uem_sys +"版本号为："+ uem_sys_version)
            uem_fesf_list = ["SfUemFesfDs.sys","SfUemFesfDt.sys","SfUemFesfIsolate.sys","SfUemFesfSupport.sys","UemFesfDataStorage.dll","UemFesfEncryptDecrypt.dll","UemFesfIconOverlay.dll","UemFesfPolicy.dll","UemFesfPolicyKeyManager.dll","UemFesfRuleEngine.dll","UemFesfUtility.dll"]
            for uem_fesf in uem_fesf_list:
                uem_fesf_version=helper_main.getFileVersion(Program_file+"\\Sangfor\\SSL\\UEM\\agent\\fesf\\"+ uem_fesf)
                self.textBrowser_2.append(uem_fesf +"版本号为："+ uem_fesf_version)  
            for uem_agent in uem_agent_list:
                uem_agent_version=helper_main.getFileVersion(Program_file+"\\Sangfor\\SSL\\UEM\\agent\\"+ uem_agent)
                self.textBrowser_2.append(uem_agent +"版本号为："+ uem_agent_version)   
            atrust_agent_list = ["UemRpcPal.dll","UemSDK.dll"]
            for atrust_agent in atrust_agent_list:
                atrust_agent_version=helper_main.getFileVersion(Program_file+"\\Sangfor\\aTrust\\aTrustAgent\\"+ atrust_agent)
                self.textBrowser_2.append(atrust_agent +"版本号为："+ atrust_agent_version)   
            atrust_core_list = ["UemSDKWrapper.dll"]
            for atrust_core in atrust_core_list:
                atrust_core_version=helper_main.getFileVersion(Program_file+"\\Sangfor\\aTrust\\aTrustAgent\\plugins\\aTrustCore\\"+ atrust_core)
                self.textBrowser_2.append(atrust_core +"版本号为："+ atrust_core_version)   
        except Exception as e:
            self.textBrowser_2.append("一键检查版本号失败！！！")
            self.textBrowser_2.append(str(e))
    def check_net_policy(self):
        try:
            p_id = self.lineEdit_13.text()   
            int(p_id)       
            a,b,c=helper_main._exec_cmd(helper_main.resource_path(os.path.join("res","exe\\TestUemRpc.exe"))+" abc abc "+p_id)
            self.textBrowser_2.setPlainText(b)
        except Exception as e:
            self.textBrowser_2.setPlainText(str(e))
    def check_user_policy_service(self):
        try:
            a,b,c=helper_main._exec_cmd(helper_main.resource_path(os.path.join("res","exe\\TestUemRpc.exe")))
            self.textBrowser_2.setPlainText(b)
        except Exception as e:
            self.textBrowser_2.setPlainText(str(e))
    def combox_ip(self):
        try:
            addr_type=self.comboBox_2.currentText()
            if addr_type == "单个IP":
                self.lineEdit_6.setPlaceholderText("例如：10.242.2.158")
            if addr_type == "IP范围":
                self.lineEdit_6.setPlaceholderText("例如：1.1.1.1-1.1.1.254")
            if addr_type == "域名":
                self.lineEdit_6.setPlaceholderText("例如：www.sangfor.com")
        except Exception as e:
            self.textBrowser.setPlainText(str(e))
    def combox_port(self):
        try:
            port_type=self.comboBox_3.currentText()
            if port_type == "单个端口":
                self.lineEdit_7.setPlaceholderText("例如：80")
            if port_type == "端口范围":
                self.lineEdit_7.setPlaceholderText("例如：80-100")
        except Exception as e:
            self.textBrowser.setPlainText(str(e))
    def connect_flush(self, u_time,des):
        self.textBrowser.append(str(des))
        self.lcdNumber_2.display("%.4f" % u_time)
        QtWidgets.QApplication.processEvents()     
    def connect_Start(self):
        try:
            connect_type=self.comboBox.currentText()
            addr_type=self.comboBox_2.currentText()
            port_type=self.comboBox_3.currentText()
            times_type=self.comboBox_4.currentText()
            ipaddr_input=self.lineEdit_6.text()
            port_input=self.lineEdit_7.text()
            times_input=self.lineEdit_8.text()
            self.pushButton_15.setEnabled(False)
            self.thread = QThread()
            self.worker = Work()
            self.worker.des_signal.connect(self.connect_flush)
            self.worker.moveToThread(self.thread)
            self.thread.finished.connect(self.connect_finished)
            self.thread.started.connect(lambda:self.worker.connect_work(ipaddr_input=ipaddr_input,port_input=port_input,connect_type=connect_type,addr_type=addr_type,port_type=port_type))
            self.thread.start()                                                                         
        except Exception as e:
            self.textBrowser.setPlainText(str(e))
    def connect_Stop(self):
        self.worker.work_stop()
        self.thread.quit()
    def connect_finished(self):
        self.pushButton_15.setEnabled(True)
    # def start_iperf3(self):
    #     try:
    #         if self.radioButton.isChecked()==True:
    #             d_ip = self.lineEdit_10.text()
    #             d_port = self.lineEdit_11.text()
    #             protocol = self.comboBox_5.currentText()
    #             if protocol == "TCP":
    #                 command =iperf3 + " -c "+d_ip+" -p "+d_port
    #             if protocol == "UDP":
    #                 command =iperf3 + " -c "+d_ip+" -p "+d_port+" -u"
    #         if self.radioButton_2.isChecked()==True:
    #             s_port = self.lineEdit_12.text()
    #             command = iperf3 +  " -s "+s_port
    #         print(command)
    #         self.pushButton_16.setEnabled(False)
    #         self.thread2 = QThread()
    #         self.worker2 = Iperf3()
    #         self.worker2.msg_signal.connect(self.flush_iperf3)
    #         self.worker2.moveToThread(self.thread2)
    #         self.thread2.finished.connect(self.finished_iperf3)
    #         self.thread2.started.connect(lambda:self.worker2.iperf3_work(command=command))
    #         self.thread2.start()   
    #     except Exception as e:
    #         self.textBrowser.setPlainText(str(e))
    # def stop_iperf3(self):  
    #     self.worker2.iperf3_stop()
    #     self.thread2.quit()
    def finished_iperf3(self):
        self.pushButton_16.setEnabled(True)
    def flush_iperf3(self,msg):
        self.textBrowser.append(msg)
        QtWidgets.QApplication.processEvents()
    def check_login_time_log(self):
        try:
            #UEM登录总流程时间
            login_start_time = helper_main.filter_log_time(log_type="aTrustCore",checkflag="Click Login",begorend="begin timeStamp")
            #login_com_time = helper_main.filter_log_time(log_type="explorer",checkflag="创建水印",begorend="end timeStamp").split(",")[0]
            login_com_time = helper_main.filter_log_time(log_type="explorer",checkflag="创建水印",begorend="begin timeStamp").strip().rstrip( '\x00' )
            login_used_time = int(login_com_time) - int(login_start_time)
            self.textBrowser_3.setPlainText("UEM登录总流程时间为："+str(login_used_time)+"ms")  
            #1.登录流程时间
            login1_start_time = helper_main.filter_log_time(log_type="aTrustCore",checkflag="Click Login",begorend="begin timeStamp")
            login1_com_time = helper_main.filter_log_time(log_type="Resource OK",checkflag="Resource OK",begorend="begin timeStamp")
            login1_used_time = int(login1_com_time) - int(login1_start_time)
            self.textBrowser_3.append("1.登录流程时间为："+str(login1_used_time)+"ms")  
            #2.UemSdkWrapper初始化时间
            sdk_start_time = helper_main.filter_log_time(log_type="Resource OK",checkflag="Resource OK",begorend="begin timeStamp")
            sdk_com_time = helper_main.filter_log_time(log_type="SfUemClient",checkflag="aWork模块",begorend="begin timeStamp").strip().rstrip( '\x00' )
            #print(sdk_start_time,sdk_com_time)
            sdk_used_time = int(sdk_com_time) - int(sdk_start_time)
            self.textBrowser_3.append("2.UemSdkWrapper初始化时间为："+str(sdk_used_time)+"ms")  
            #3.awork初始化时间
            awork_start_time = helper_main.filter_log_time(log_type="SfUemClient",checkflag="aWork模块",begorend="begin timeStamp").strip().rstrip( '\x00' )
            awork_com_time = helper_main.filter_log_time(log_type="explorer",checkflag="加载UnifiedHook.dll回调",begorend="begin timeStamp").strip().rstrip( '\x00' )
            #print(awork_start_time,awork_com_time)
            awork_used_time = int(awork_com_time) - int(awork_start_time)
            self.textBrowser_3.append("3.Awork初始化时间为："+str(awork_used_time)+"ms")  
            #4.Explorer初始化时间
            explorer_start_time = helper_main.filter_log_time(log_type="explorer",checkflag="加载UnifiedHook.dll回调",begorend="begin timeStamp").strip().rstrip( '\x00' )
            explorer_com_time = helper_main.filter_log_time(log_type="explorer",checkflag="创建水印",begorend="begin timeStamp").strip().rstrip( '\x00' )
            explorer_used_time = int(explorer_com_time) - int(explorer_start_time)
            self.textBrowser_3.append("4.Explorer初始化时间为："+str(explorer_used_time)+"ms")  
            #每个小阶段具体时间
            appdata_checkflags = ['Login Success', 'Load Uem SDK', 'Resource OK', 'after resource ok WrapperSDk Module', 'Load Uem SDK', 'Check Uem Update', 'Start Uem', 'Set Uem Policy', 'Set Uem Net Rule', 'Prepare Enter SandboxSpace', 'Set Work Mode', 'Notify UemAgent Enter', 'Create SfUemClient Process']
            for checkflag in appdata_checkflags:
                aTrustCore_time = helper_main.filter_log_time(log_type="aTrustCore",checkflag=checkflag,begorend="end timeStamp").strip().split(",")[-1]
                self.textBrowser_3.append(checkflag+" "+aTrustCore_time+"ms")
                QtWidgets.QApplication.processEvents()
            SfUemClient_checkflags = ['aWork模块', 'aWork进程创建', '等待UemAgent服务Ready', '等待UemAgent策略Ready', '准备进入桌面', '创建桌面对象', '创建Explorer进程', '切换桌面']
            for checkflag in SfUemClient_checkflags:
                aTrustCore_time = helper_main.filter_log_time(log_type="SfUemClient",checkflag=checkflag,begorend="end timeStamp").strip().split(",")[-1]
                self.textBrowser_3.append(checkflag+" "+aTrustCore_time+"ms")
                QtWidgets.QApplication.processEvents()
            explorer_checkflags = ['加载UnifiedHook.dll回调', 'Hook dll初始化', '加载桌面', 'UemDesktopSpace模块', 'UemDesktopSpace.dll初始化', '初始化Gdi', '创建安全桌面工具栏', '设置安全桌面壁纸', '创建安全桌面工具栏', '设置安全桌面壁纸', '创建水印']
            for checkflag in explorer_checkflags:
                aTrustCore_time = helper_main.filter_log_time(log_type="explorer",checkflag=checkflag,begorend="end timeStamp").strip().split(",")[-1]
                self.textBrowser_3.append(checkflag+" "+aTrustCore_time+"ms")
                QtWidgets.QApplication.processEvents()                
        except Exception as e:
            self.textBrowser_3.append(str(e))     
    def check_audit_allip_log(self):   
        try:
            public_path = os.getenv('PUBLIC')   
            log_path = public_path + "\\Sangfor\\SSL\\UEM\\Log\\UemMonitor.exe.log"
            for line in open(log_path,encoding='gbk',errors='ignore'):
                if "Proxy json data:" in line:
                    audit_allip_org = line
            self.textBrowser_3.setPlainText(audit_allip_org)
            audit_allip = audit_allip_org.split("Proxy json data:")[1]
            audit_ip_list = audit_allip.split("[")[1].split("]")[0].split(",")
            for audit_ip in audit_ip_list:
                for line1 in open(log_path,encoding='gbk',errors='ignore'):
                    if eval(audit_ip) in line1:
                        audit_ip_status = line1               
                audit_ip_status_new = audit_ip_status.split("_DetectProxyTask end,")[1]
                self.textBrowser_3.append(audit_ip_status_new)
        except Exception as e:
            self.textBrowser_3.setPlainText(str(e)) 
    def check_audit_FileExport_log(self):   
        try:
            public_path = os.getenv('PUBLIC')   
            log_path = public_path + "\\Sangfor\\SSL\\UEM\\Log\\UemFileExport.exe.log"
            for line in open(log_path,encoding='gbk',errors='ignore'):
                if "_DoFileCheckReport url" in line:
                    audit_FileExport_org = line
            self.textBrowser_3.setPlainText(audit_FileExport_org)
        except Exception as e:
            self.textBrowser_3.setPlainText(str(e)) 
    def check_audit_clipboard_log(self):   
        try:
            public_path = os.getenv('PUBLIC')   
            log_path = public_path + "\\Sangfor\\SSL\\UEM\\Log\\UemCheckTool.exe.log"
            for line in open(log_path,encoding='gbk',errors='ignore'):
                if "_DoClipCheckReport url" in line:
                    audit_clipboard_org = line
            self.textBrowser_3.setPlainText(audit_clipboard_org)
        except Exception as e:
            self.textBrowser_3.setPlainText(str(e)) 
    def start_procexp(self):
        try:
            os.startfile(helper_main.resource_path(os.path.join("res","exe\\procexp.exe")))
        except Exception as e:
            self.textBrowser_4.setPlainText(str(e)) 
    def start_ResHacker(self):
        try:
            os.startfile(helper_main.resource_path(os.path.join("res","exe\\ResHacker.exe")))
        except Exception as e:
            self.textBrowser_4.setPlainText(str(e)) 
    def start_Procmon(self):
        try:
            os.startfile(helper_main.resource_path(os.path.join("res","exe\\Procmon.exe")))
        except Exception as e:
            self.textBrowser_4.setPlainText(str(e)) 
    def start_hash(self):
        try:
            os.startfile(helper_main.resource_path(os.path.join("res","exe\\hash_1.0.4.exe")))
        except Exception as e:
            self.textBrowser_4.setPlainText(str(e)) 
    def start_fvie(self):
        try:
            os.startfile(helper_main.resource_path(os.path.join("res","exe\\FVIE.exe")))
        except Exception as e:
            self.textBrowser_4.setPlainText(str(e)) 
    def start_DebugView(self):
        try:
            os.startfile(helper_main.resource_path(os.path.join("res","exe\\DebugView.exe")))
        except Exception as e:
            self.textBrowser_4.setPlainText(str(e)) 
    def collect_app_info(self):
        try:
            file_path = self.lineEdit_9.text()
            app_info_cmd = helper_main.resource_path(os.path.join("res","exe\\GetPeInfoTool.exe")) + ' ' +'"' + file_path + '"'
            a,b,c=helper_main._exec_cmd(app_info_cmd)
            self.textBrowser_4.setPlainText(b) 
        except Exception as e:
            self.textBrowser_4.setPlainText(str(e)) 
    def save_app_info(self):
        try:
            file_path = self.lineEdit_9.text()
            app_info_cmd = helper_main.resource_path(os.path.join("res","exe\\GetPeInfoTool.exe")) + ' ' +'"' + file_path + '"'
            app_name = self.lineEdit_10.text()
            app_tag = self.lineEdit_11.text()
            app_des = self.lineEdit_12.text()
            excel_path = self.lineEdit_14.text()
            excel_path_rel = excel_path+'/source.csv'
            app_file_name = str(file_path).split('/')[-1].split('\\')[-1]
            a,b,c=helper_main._exec_cmd(app_info_cmd)
            #获取原始文件夹名
            orig_name_org = b.split("\n")[6].encode('gbk').decode('gbk')
            if ':' in orig_name_org:
                app_orig_name = orig_name_org.split(":")[1].strip().replace('\x00', '').strip()
            else:
                app_orig_name = ''
            #获取签名
            signature_org = b.split("\n")[8].encode('gbk').decode('gbk')
            if ':' in signature_org:
                app_signature = signature_org.split(":")[1].strip().replace('\x00', '').strip()
            else:
                app_signature = ''
            if os.path.exists(excel_path_rel):
                r_xls = xlrd.open_workbook(excel_path_rel)
                row = r_xls.sheets()[0].nrows
                excel = copy(r_xls)
                table = excel.get_sheet(0)
                table.write(row,0,app_name)
                table.write(row,1,app_des)
                table.write(row,2,app_tag)
                table.write(row,3,app_file_name)
                table.write(row,4,app_orig_name)
                table.write(row,5,app_signature)
                table.write(row,6,"2")
                excel.save(excel_path_rel)
                self.textBrowser_4.setPlainText(app_name+"程序信息追加成功，Excel存放路径："+excel_path_rel)
            else:
                newb=xlwt.Workbook(encoding='utf-8') 
                nws=newb.add_sheet('source') 
                nws.write(0,0,'name') 
                nws.write(0,1,'description')
                nws.write(0,2,'tag_list')
                nws.write(0,3,'process_name')
                nws.write(0,4,'orig_name')
                nws.write(0,5,'signature')
                nws.write(0,6,'type')
                nws.write(1,0,app_name)
                nws.write(1,1,app_des)
                nws.write(1,2,app_tag)
                nws.write(1,3,app_file_name)
                nws.write(1,4,app_orig_name)
                nws.write(1,5,app_signature)
                nws.write(1,6,"2")
                newb.save(excel_path_rel)
                self.textBrowser_4.setPlainText(app_name+"程序信息生成成功，Excel存放路径："+excel_path_rel)
        except Exception as e:
            self.textBrowser_4.setPlainText(str(e))
class Work(QObject):
    des_signal = pyqtSignal(float,str)
    def __init__(self):
        super(Work, self).__init__()
        self.run = True
    def connect_work(self,ipaddr_input,port_input,connect_type,addr_type,port_type):
        print(ipaddr_input,port_input,connect_type,addr_type,port_type)
        self.run = True
        try:
            if addr_type == "单个IP":
                if port_type == "单个端口":
                    if connect_type == "TELNET":
                        u_time,des = helper_main.telnet_time(addr=ipaddr_input,telnet_port=port_input)
                        #print(u_time,des)
                        self.des_signal.emit(u_time,des)      
                    if connect_type == "HTTP":
                        url = "http://"+ipaddr_input+":"+port_input
                        u_time,r_info=helper_main.http_s_time(url)
                        self.des_signal.emit(u_time,r_info)     
                    if connect_type == "HTTPS":
                        url = "https://"+ipaddr_input+":"+port_input
                        u_time,r_info=helper_main.http_s_time(url)
                        self.des_signal.emit(u_time,r_info)     
                if port_type == "端口范围":
                    #将端口范围变成端口数组
                    portx = port_input.split('-')
                    port_list = list(range(int(portx[0]),int(portx[1])+1))
                    for t_port in port_list:
                        if connect_type == "TELNET":
                            print(ipaddr_input,t_port)
                            u_time,des = helper_main.telnet_time(addr=ipaddr_input,telnet_port=t_port)
                            #print(u_time,des)
                            self.des_signal.emit(u_time,des)
                        if connect_type == "HTTP":
                            url = "http://"+ipaddr_input+":"+str(t_port)
                            u_time,r_info=helper_main.http_s_time(url)
                            self.des_signal.emit(u_time,r_info)     
                        if connect_type == "HTTPS":
                            url = "https://"+ipaddr_input+":"+str(t_port)
                            u_time,r_info=helper_main.http_s_time(url)
                            self.des_signal.emit(u_time,r_info)     
            if addr_type == "IP范围":
                    #将IP范围变成IP数组
                    ipx = ipaddr_input.split('-')
                    ip2num = lambda x:sum([256**i*int(j) for i,j in enumerate(x.split('.')[::-1])])
                    num2ip = lambda x: '.'.join([str(x//(256**i)%256) for i in range(3,-1,-1)])
                    ip_list = [num2ip(i) for i in range(ip2num(ipx[0]),ip2num(ipx[1])+1) if not ((i+1)%256 == 0 or (i)%256 == 0)]
                    if port_type == "单个端口":
                        for ipaddr in ip_list:
                            if connect_type == "TELNET":
                                u_time,des = helper_main.telnet_time(addr=ipaddr,telnet_port=port_input)
                                self.des_signal.emit(u_time,des)
                            if connect_type == "HTTP":
                                url = "http://"+ipaddr+":"+port_input
                                u_time,r_info=helper_main.http_s_time(url)
                                self.des_signal.emit(u_time,r_info)     
                            if connect_type == "HTTPS":
                                url = "https://"+ipaddr+":"+port_input
                                u_time,r_info=helper_main.http_s_time(url)
                                self.des_signal.emit(u_time,r_info)   
                    if port_type == "端口范围":
                        #将端口范围变成端口数组
                        portx = port_input.split('-')
                        port_list = list(range(int(portx[0]),int(portx[1])+1))
                        for ipaddr in ip_list:
                            for t_port in port_list:
                                if connect_type == "TELNET":
                                    u_time,des = helper_main.telnet_time(addr=ipaddr,telnet_port=t_port)
                                    self.des_signal.emit(u_time,des)
                                if connect_type == "HTTP":
                                    url = "http://"+ipaddr+":"+str(t_port)
                                    u_time,r_info=helper_main.http_s_time(url)
                                    self.des_signal.emit(u_time,r_info)     
                                if connect_type == "HTTPS":
                                    url = "https://"+ipaddr+":"+str(t_port)
                                    u_time,r_info=helper_main.http_s_time(url)
                                    self.des_signal.emit(u_time,r_info)     
        except Exception as e:
            self.des_signal.emit(9.9999,str(e))  
            self.run = False
    def work_stop(self):
        self.run = False
# class Iperf3(QObject):
#     msg_signal = pyqtSignal(str)
#     def __init__(self):
#         super(Iperf3, self).__init__()
#         self.run = True
#     def iperf3_work(self,command):
#         self.run = True
#         try:
#             a,b,c=helper_main._exec_cmd(command)
#             print(b)
#             self.msg_signal.emit(str(b))
#         except Exception as e:
#             self.msg_signal.emit(str(e))
#     def iperf3_stop(self):
#         self.run = False
class Uem_collect(QObject):
    msg_signal = pyqtSignal(str)
    def __init__(self):
        super(Uem_collect, self).__init__()
        self.run = True
    def collect_work(self,folder_path):
        self.run = True
        ueminfo_path =folder_path+"/ueminfo_collect"
        print(ueminfo_path)
        try:
            self.msg_signal.emit("正在收集环境信息...") 
            environment_path=ueminfo_path+"/environment/"
            os.makedirs(environment_path) 
            #收集systeminfo信息
            helper_main.windows_systeminfo(environment_path)
            #收集进程列表和模块列表
            helper_main.process_module_info(environment_path)
            helper_main.uem_version_info(environment_path)
            #收集软件列表
            helper_main.software_info(environment_path)
            self.msg_signal.emit("环境信息收集成功！")  
            QtWidgets.QApplication.processEvents() 
        except Exception as e:
            self.msg_signal.emit("环境信息收集失败！！！") 
            self.msg_signal.emit(str(e)) 
        try:
            self.msg_signal.emit("正在收集日志信息...") 
            #self.textBrowser_6.append("正在收集日志信息...")
            log_path=ueminfo_path+"/log/"
            os.makedirs(log_path)
            #收集dump日志
            #helper_main.dump_log(log_path)
            #收集windows事件日志
            helper_main.uem_log(log_path)
            #收集UEM相关日志
            helper_main.windows_log(log_path)
            self.msg_signal.emit("日志信息收集成功！") 
            #self.textBrowser_6.append("日志信息收集成功！")
        except Exception as e:
            self.msg_signal.emit("日志信息收集失败！！！") 
            #self.textBrowser_6.append("日志信息收集失败！！！")
            self.msg_signal.emit(str(e)) 
            #self.textBrowser_6.append(str(e))
        ueminfo_zip=folder_path+"/ueminfo_collect.zip"
        helper_main.compressFolder(ueminfo_path, ueminfo_zip)
        success_result="UEM终端信息一键收集完成！"+"终端信息收集文件为："+ ueminfo_zip
        #self.textBrowser_6.append(success_result)
        self.msg_signal.emit(success_result) 
        self.run = False

if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    ui = mywindow()    
    ui.show()
    sys.exit(app.exec_())





