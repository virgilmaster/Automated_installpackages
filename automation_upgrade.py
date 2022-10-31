# Author: Virgil
# Functions: To download the python packages from internet automactically
# Email-address: 691267837@qq.com
# Date: 2022/10/28
# Company: Intel
# Version: 0.0.3

import os
from string import punctuation
import string
from struct import pack
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
import logging



    

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
    print('=======================================================================================================================================')
    print('WOW, your system is: ' + operation_system + '!!!')
    print("Start to check whether the python packages is intalled or not?")
    print("You have installed the following installation package: ")


def handle_packages(output_num,pack_information): 
    numbers = int(output_num) 
    for i in (0,numbers-4,numbers-3,numbers-2,numbers-1):
        package_detail = str(pack_information[i])
        package_result = package_detail.split("'")[1].split("'")[0]
        package_names = package_result.split("==")[0]  # The package's names
        package_version = package_result.split("==")[1] # The packages's version
        final_version = re.sub('[%s]' % re.escape(string.punctuation), '', package_version)
        print(final_version)
        
        if operation_system == "Windows":
            packages_installed = os.popen("pip list | findstr " + package_names)
            result_installed = packages_installed.read()
            packages_installed.close()
            installed_version = result_installed.split(" ")[-1]
            final_installed = re.sub('[%s]' % re.escape(string.punctuation), '', installed_version)
            print(final_installed)
            while final_installed == final_version:
                print("Your " + package_names + " 's version is correct have no necessary to install")
            else:
                print("Your " + package_names + " 's version is not correct")

        elif operation_system == "Linux":
            packages_installed = os.popen("pip list | grep " + package_names)
            result_installed = packages_installed.read()
            packages_installed.close()


    
if __name__ == "__main__":
    #start_counter = time.perf_counter()
    file_name = 'requirements.txt'
    read_requirements(file_name)
    operation_system = platform.system()
    pack_information = read_requirements(file_name)
    check_packages()
    if operation_system == "Windows":
        pack_num = os.popen('type requirements.txt | find /v /c""')
        output_num = pack_num.read()
        pack_num.close()
    elif operation_system == "Linux":
        pack_num = os.popen('cat requirements.txt | wc -l"')
        output_num = pack_num.read()
        pack_num.close()
    handle_packages(output_num,pack_information)
    #package_detail = str(pack_information[i])
    #convert_detail(package_detail)
    # end_counter = time.perf_counter()
    # runtime = end_counter - start_counter
    # counter_process(runtime)


    #print(fd)
    #punctuation = "[',] "
    # print(re.sub(r"[%s]+" %punctuation, "",step_test))
    # test_result = re.sub(r"[%s]+ punctuation", " ",step_test)
    # print(test_result)
    #print(re.sub(r"[%s]+" str(punctuation), str(pack_information[1])))
    #print(pack_information[2])
    




        




    
    
