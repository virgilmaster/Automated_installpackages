# Author: Virgil.babala
# Functions: To download the python packages from internet automactically
# Email-address: 691267837@qq.com
# Date: 2022/10/31
# Version: 0.0.7
# Fundation: Virgil@copyright.org

import os
import re,string
import time
import datetime
import sys
import platform
import socket
from unittest import result
import urllib.request
import urllib.error
import requests
import win32api, win32con


def read_requirements(file_name):
    pack_information = []
    file = open(file_name,'r')
    file_pack_information = file.readlines()
    for row in file_pack_information:
        tmp_list = row.split(' ')
        tmp_list[-1] = tmp_list[-1].replace('\n',',')
        pack_information.append(tmp_list)
    return pack_information


def check_packages():
    print('Dear guests,begin to check your system: ')
    counter1 = 0
    while counter1 < 6:
        time.sleep(1)
        print('=======================================================================================================================================')
        counter1 += 1
    time.sleep(3)
    print('Welcome to use my scripts,hope to help you')
    print('WOW, your system is: ' + operation_system + '!!!')
    print("Start to check whether the python packages is intalled or not: ")
    print("You have installed the following installation package: ")


def handle_packages(output_num,pack_information):
    mirror_pools = {"pypi.tuna.tsinghua.edu.cn": "https://pypi.tuna.tsinghua.edu.cn/simple",
                    "pypi.douban.com": "http://pypi.douban.com/simple/",
                    "mirrors.aliyun.com": "http://mirrors.aliyun.com/pypi/simple/",
                    "pypi.mirrors.ustc.edu.cn":"https://pypi.mirrors.ustc.edu.cn/simple/"}

    with open("Mirrors_links.json","w") as mirrors_file:
        mirrors_file.write(str(mirror_pools))
        mirrors_file.close()

    numbers = int(output_num) 
    for i in (0,numbers-4,numbers-3,numbers-2,numbers-1):
        package_detail = str(pack_information[i])
        package_result = package_detail.split("'")[1].split("'")[0]
        converted_result = package_result.split(",")[0]
        print(converted_result)
        package_names = package_result.split("==")[0]  
        package_version = package_result.split("==")[1]

        with open("Download_record.txt","w") as donwload_file: # Not wonderful functions
            current_time = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
            donwload_file.write(str(username) + " have downloaded the " + package_names + " at time: " + current_time)
            donwload_file.close()
        final_version = re.sub('[%s]' % re.escape(string.punctuation), '', package_version)
        

        
        if operation_system == "Windows":
            packages_installed = os.popen("pip list | findstr " + package_names)
            result_installed = packages_installed.read()
            packages_installed.close()
            installed_version = result_installed.split(" ")[-1]
            final_installed = re.sub('[%s]' % re.escape(string.punctuation), '', installed_version)
            
            while final_installed == final_version:
                print("Your " + package_names + "'s version is correct have no necessary to install")
                time.sleep(3)
                sys.exit
            else:
                print("Your " + package_names + "'s version is not correct")
                os.system("echo " + "powershell " + ">" + "launch_powershell.bat")
                #os.system("pip install " + converted_result + " -i http://pypi.douban.com/simple/" + " --trusted-host " + "pypi.douban.com")
                
        elif operation_system == "Linux":
            packages_installed = os.popen("pip list | grep " + package_names)
            result_installed = packages_installed.read()
            packages_installed.close()
            installed_version = result_installed.split(" ")[-1]
            final_installed = re.sub('[%s]' % re.escape(string.punctuation), '', installed_version)
            
            while final_installed == final_version:
                print("Your " + package_names + "'s version is correct have no necessary to install")
                time.sleep(3)
                sys.exit
            else:
                print("Your " + package_names + "'s version is not correct")


                    

            
def counter_process(runtime):
    scale = 100
    print("Start downloading the python packages".center(scale // 2, "-"))
    for i in range(scale + 1):
        conuter1 = ">" * i
        counter2 = "-" * (scale - i)
        counter3 = (i / scale) * 100
        print("\r{:^3.0f}%[{}>{}]{:.2f}s".format(counter3, conuter1, counter2, runtime), end="")
        time.sleep(0.1)
    print("\n" + "All the job is done,lucky so much".center(scale // 2, "-"))

    



if __name__ == "__main__":
    start_counter = time.perf_counter()
    file_name = 'requirements.txt'
    read_requirements(file_name)
    operation_system = platform.system()
    pack_information = read_requirements(file_name)
    check_packages()
    if operation_system == "Windows":
        pack_num = os.popen('type requirements.txt | find /v /c""')
        username = os.getlogin()
        output_num = pack_num.read()
        pack_num.close()
    elif operation_system == "Linux":
        pack_num = os.popen('cat requirements.txt | wc -l"')
        command_username = os.popen('whoami')
        username = command_username.read()
        output_num = pack_num.read()
        command_username.close()
        pack_num.close()
    handle_packages(output_num,pack_information)


    end_counter = time.perf_counter()
    runtime = end_counter - start_counter
    counter_process(runtime)
    win32api.MessageBox(0, "All installation items have been completed","Installation tips",win32con.MB_OK)






        




    
    
