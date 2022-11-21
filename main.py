# Author: Virgil.She
# Date: 2022/11/21
# Version: 0.2.23
# Introduction: A fans of python programming language

import os
import re,string
import time,datetime
import platform
from filehandler import filesdetails
from multiprocessing import Process,Lock
import threading
from queue import Queue
from artist import logwriter
from progessbar import timebar

def check_system(operation_system):
    print('Dear guests,begin to check your system: ')    
    counter1 = 0 
    while counter1 < 6:
        time.sleep(1)
        print('{:=^89}'.format("Checking"))
        counter1 += 1
    time.sleep(1)
    print('Your system is: ' + operation_system + '...')

def handle_packages(pack_information):
    try:
        # 导入巫师
        #from beesfly import wizard
        # 导入检查官
        from inspector import checker
    except ImportError as e:
        raise e
    # 以下代码进行重构 使用类设计模式 进行全盘重构
    # 启动 队列 中的线程任务 
    # 线程的方法正确的应该是在这边进行 导入

    final_num = files_read.counter
    numbers = int(final_num)

    for i in range(numbers):  
        package_detail = str(pack_information[i]) 
        package_result = package_detail.split("'")[1].split("'")[0]
        package_names = package_result.split("==")[0]  
        package_version = package_result.split("==")[1]
        final_version = re.sub('[%s]' % re.escape(string.punctuation), '', package_version)

        
        if operation_system == "Windows":
            packages_installed = os.popen("pip list | findstr " + package_names) 
            result_installed = packages_installed.readlines()     
            packages_installed.close()                              
            installed_version = str(result_installed).split(" ")[-1]
            final_installed = (re.sub('[%s]' % re.escape(string.punctuation), '', installed_version)).replace("n","")
            print('{:=^89}'.format("Line"))

            uninstall = []
            if installed_version == '[]':
                print(package_names +  " have not be installed")
                print("Start launch the webspiders,to download the new " + package_names)
                uninstall.append(package_names)
            elif final_installed == final_version:
                print("The " + package_names + " is in the same version,no necessary to install " + package_names + " again")

            else:
                print("The packages's version is " + installed_version)
                print("Start to change " + package_names + "'s version,plz wait a moment~.~")
                uninstall.append(package_names)

                
            

        elif operation_system == "Linux":
            os.system('alias python=' + 'python3')
            packages_installed = os.popen("pip list | grep " + package_names) 
            result_installed = packages_installed.readlines()     
            packages_installed.close()
            installed_version = str(result_installed).split(" ")[-1]
            final_installed = (re.sub('[%s]' % re.escape(string.punctuation), '', installed_version)).replace("n","")
            print('{:=^89}'.format("Line"))

            if installed_version == '[]':
                print(package_names +  " have not be installed")
                print("Start launch the webspiders,to download the new " + package_names)
                
            elif final_installed == final_version:
                print("The " + package_names + " is in the same version,no necessary to install " + package_names + " again")
            else:
                print("The packages's version is " + installed_version)
                print("Start to change" + package_names + "'s version,plz wait a moment~.~")


if __name__ == "__main__":
    start_counter = time.perf_counter()
    os_result = platform.system()
    print("Begin time is: " + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    files_read = filesdetails(str(os_result),'requirements.txt')
    operation_system = platform.system()
    pack_information = files_read.readinfo
    check_system(operation_system)
    handle_packages(pack_information)
    launcher = logwriter(operation_system,pack_information)
    launcher.log_record()
    print("End time is: " + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    end_counter = time.perf_counter()
    runtime = timebar(start_counter,end_counter)
    runtime.counter_process()
