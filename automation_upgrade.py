import os
import time
import datetime
import sys
import platform
import socket
from unittest import result
import urllib.request
import urllib.error


# Class

def main():
    start = time.perf_counter()
    #交互式
    #packages_install = input('Please enter the Python package you want to install: ')
    #print('The Python package you want to install is: ', packages_install)
    check_packages()
    install_packages()
    end = time.perf_counter()
    runtime = end - start
    counter_process(runtime)


def check_packages():
    # 打开检查功能
    # This function can read the requirement.txt by readline and to install the correct version of packages
    # 检查功能: 
    with open('requirements.txt','r') as require_file:
        read_requirement = require_file.readlines()
        for i,line in enumerate(read_requirement):
            # 结果没有遍历出来
            packages_version = line.split('==')[1]  # 客户想要安装包的版本
            install_packages = line.split('==')[0]  # 客户想要安装的包
            # 测试功能正常
            #print(packages_version)
            print(install_packages)

    operation_system = platform.system()
    print("Start to check whether the Python package is installed")
    if (operation_system == 'Windows'):
        os.system('pip list | findstr ' + install_packages + '> ' + ' checkresult.txt')
        username = os.getlogin()
        with open('checkresult.txt','r') as result_file:
            result = result_file.readlines()
            for i, line in enumerate(result):
                current_version = line.split(' ')[-1]  # 当前电脑包的版本
                current_packages = line.split(' ')[0]  # 当前电脑包
        print(current_packages)
        print('Dear guests your operation system is: ' + operation_system + ' The ' + install_packages + ' in you laptop is version:' + current_version)

    elif (operation_system == 'Linux'):
        os.system('pip list | grep ' + install_packages + '> ' + ' checkresult.txt')
        username = os.system('whoami')
        with open('checkresult.txt','r') as result_file:
            result = result_file.readlines()
            for i, line in enumerate(result):
                current_version = line.split(' ')[-1]  # 当前电脑包的版本
                current_packages = line.split(' ')[0]  # 当前电脑包
        print('Dear guests your operation system is: ' + operation_system + ' The ' + install_packages + ' in you laptop is version:' + current_version)


    
    # 交互式功能
    # with open('checkversion.txt','r') as file:
    #     packages_result = file.read()
    #     version_result = (file.read()).split(' ')[-1]
    #     print(packages_result.split(' ')[0])
    #     print(version_result)

    # 判断安装包是否存在: 有一个包存在了就终止了会有BUG 难道是多线程？说明没有遍历出来
    # while install_packages == current_packages:
    #     print(install_packages + " has been installed on this computer")
    #     #sys.exit()       
    # else:
    #     print("Start to checkout the version of " + install_packages + " you want to installed in this laptop")
    # 判断安装包的版本信息是否匹配:
    # while packages_version == current_version:
    #     print(install_packages + " is the same version on this computer,no more to upgrade!!!")
    #     #sys.exit()
    # else:
    #     print("Start to setup the " + install_packages + " you want to installed in this laptop")

    if os.path.exists("packages_log.txt") == True:
        with open("packages_log.txt", "w") as file:
            current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            file.write(str(username) + " downloaded the " + install_packages + " downloaded time: " + current_time)
    else:
        if (operation_system == 'Windows'):
            with open("packages_log.txt", "w") as logfile:
                current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                logfile.write(str(username) + " downloaded the " + install_packages + " downloaded time: " + current_time)

        elif (operation_system == 'Linux'):
            with open("packages_log.txt", "w") as logfile:
                current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                logfile.write(str(username) + " downloaded the " + install_packages + " downloaded time: " + current_time)


# Addtional function to add more link pools in the dictionary.
# Installing the packages 
# The first step is to check the version
# The second step is to install the packages
def install_packages():
    mirrors_pool = {"pypi.tuna.tsinghua.edu.cn": "https://pypi.tuna.tsinghua.edu.cn/simple",
                    "pypi.douban.com": "http://pypi.douban.com/simple/",
                    "mirrors.aliyun.com": "http://mirrors.aliyun.com/pypi/simple/"}

    
    with open("mirrors_links.txt", "w") as mirrorsfile:
        mirrorsfile.write(str(mirrors_pool))
        mirrorsfile.close()

    # CDing the functions will more powerfule.Use the beautiful Algorithm to make the programe more wonderful.Learn to use dictionary.
    # 2022-10-24: Today's aim is to slove this function.
    # 2022-10-25: Today use while loop to slove this problem 
    # while version_install == version_result:
    #     print()

    # logical problems:
    # try:
    #     pip_install = os.system('pip install ' + packages_install + " -i https://pypi.tuna.tsinghua.edu.cn/simple" + ' --trusted-host ' + " pypi.tuna.tsinghua.edu.cn")
    #     response_tsing = urllib.request.urlopen('https://pypi.tuna.tsinghua.edu.cn',timeout=5)
    # except urllib.error.URLError as e:
    #     if isinstance(e.reason, socket.timeout):
    #         print('tsinghua requested timeout')
    # try:
    #     pip_install = os.popen('pip install ' + packages_install + " -i http://pypi.douban.com/simple/" + ' --trusted-host ' + " pypi.douban.com")
    #     response_douban = urllib.request.urlopen('http://pypi.douban.com',timeout=20)
    # except urllib.error.URLError as e1:
    #     if isinstance(e1.reason, socket.timeout):
    #         print('douban requested timeout')
    # try:
    #     pip_install = os.popen('pip install ' + packages_install + " -i http://mirrors.aliyun.com/pypi/simple/" + ' --trusted-host ' + " mirrors.aliyun.com")
    #     response_aliyun = urllib.request.urlopen('http://mirrors.aliyun.com',timeout=15)
    # except urllib.error.URLError as e2:
    #     if isinstance(e2.reason, socket.timeout):
    #         print('aliyun requested timeout')
    
    # Function: 安装完之后在把，安装版本的信息写进去


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


main()


