# Author: Virgil
# Functions: to download the python packages from internet
# Email-address: yefengx.he@intel.com
# Date: 2022/10/28
# Company: Intel
# Version: 0.0.1

import os
from string import punctuation
from struct import pack
import re
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

#from installation import counter_process



def main():
    #start_counter = time.perf_counter()
    file_name = 'requirements.txt'
    read_requirements(file_name)
    operation_system = platform.system()
    pack_information = read_requirements(file_name)
    check_system(operation_system)
    packages_counter = 1
    loop_function(packages_counter,pack_information)
    step_test = loop_function(packages_counter,pack_information)
    check_packages(step_test)
    # end_counter = time.perf_counter()
    # runtime = end_counter - start_counter
    # counter_process(runtime)
    

def read_requirements(file_name):
    pack_information = []
    file = open(file_name,'r')
    file_pack_information = file.readlines()
    for row in file_pack_information:
        tmp_list = row.split(' ')
        tmp_list[-1] = tmp_list[-1].replace('\n',',')
        pack_information.append(tmp_list)
    return pack_information


def check_system(operation_system):
    print('Dear guests,begin to check your system: ')
    counter1 = 0
    while counter1 < 6:
        time.sleep(1)
        print('==============================================================================')
        counter1 += 1
    time.sleep(3)
    print('==============================================================================')
    print('WOW, your system is: ' + operation_system + '!!!')
    print("Start to check whether the python packages is intalled or not?!!=.=")

    

def loop_function(packages_counter,pack_information):
    pack_num = os.popen('type requirements.txt | find /v /c""')
    output_num = pack_num.read()
    pack_num.close()
    while packages_counter < int(output_num):
        step_test = str(pack_information[packages_counter])
        packages_counter += 1
    return step_test


def check_packages(step_test):
    # step_test = str(pack_information[2])
    # print(step_test)
    result = step_test.split("'")[1].split("'")[0]
    #print(result)
    convert_result = result.split("==")[0]
    os.system("pip list | findstr " + convert_result)


    #print(fd)
    #punctuation = "[',] "
    # print(re.sub(r"[%s]+" %punctuation, "",step_test))
    # test_result = re.sub(r"[%s]+ punctuation", " ",step_test)
    # print(test_result)
    #print(re.sub(r"[%s]+" str(punctuation), str(pack_information[1])))
    #print(pack_information[2])
    
    # ∴ => pack_information[n]
    # 综上所述=> 什么啊? 当 while 行数 小于  
    # This function is to check the result from the text book: it's automation
    # if (operation_system == 'Windows'):
    #     check_command = os.popen('pip list | findstr ' + test_result)
    #     print(check_command)


main()

        


    

# def main():
#     start = time.perf_counter()
#     operation_system = platform.system()
#     file_name = 'requirements.txt'
#     open_readtxt(file_name)
#     check_system(operation_system)
#     # check_version()
#     # install_packages()
#     end = time.perf_counter()
#     runtime = end - start
#     # counter_process(runtime)
#     print(pack_information)


    

# def check_system(operation_system):
#     # file = open("requirements.txt","r")
#     print('Dear guests,begin to check your system: ' + operation_system)
#     if (operation_system == 'Windows'):
#         pack_num = os.popen('type requirements.txt | find /v /c""')
#         output_num = pack_num.read()
#         pack_num.close()
        #print(output_num)
        # print(type(output_num))
        # pack_infile1 = file.readlines()[-1].split("'=")[0]
        # print(pack_infile1)
        # [$num] 里的$num 为正序或者负序  0 到 正数 
        # 理解了
        # pack_infile1 = file.readlines()[-3].split("==")[0]
        # print(pack_infile1)
        
        # pack_infilelist = []
        # pack_infile = file.readlines()
        # result = pack_infile.append(pack_infilelist)
        # print(result)
        # for int(output_num) in file.readlines()[i]:
        #     file.readlines()[i-1]
        # n = 0
        # while n <= int(output_num):
        #     pack_infile = file.readline(n) #.split("==")[-1]
        #     n += 1
        #     result = pack_infilelist.append(pack_infile)
        #     print(pack_infilelist)
        # print(pack_infilelist)
        # 目前卡点 列表遍历
        # pack_infilelist = []
        # n = 0
        # #m = 0
        # while n <= int(output_num):
        #     pack_infile = file.readline(n).split("==")[0]
        #     n += 1
        #     result = pack_infilelist.append(pack_infile)
        # print(result[0])

                

        #print(pack_infile2)

        # pack_infilelist = []
        # n = 0

        # while n < int(output_num):
        #     print(n)
        #     pack_infile = file.readline(n).split("==")[0]
        #     print(pack_infile)
        #     n += 1
        #     pack_infilelist.append(pack_infile)
        # print(pack_infilelist)

        # j = 0
        # while j < output_num:
        #     result = os.popen('pip list | findstr ' + pack_infile)
        #     j += 1
        #     return result

    # elif (operation_system == 'Linux'):

    # elif (operation_system == 'Debian'):

    
    
