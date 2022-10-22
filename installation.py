import os
import time
import datetime
import sys
import platform
# import socket
# import urllib.request
# import urllib.error
# import jmespath


# Class

def main():
    start = time.perf_counter()
    packages_install = input('Please enter the Python package you want to install: ')
    print('The Python package you want to install is: ', packages_install)
    check_packages(packages_install)
    install_packages(packages_install)
    end = time.perf_counter()
    runtime = end - start
    counter_process(runtime)


def check_packages(packages_install):
    operation_system = platform.system()
    print("Start to check whether the Python package is installed")
    if (operation_system == 'Windows'):
        command_result = os.system('pip list | findstr ' + packages_install + '> ' + ' checkversion.txt')
        print('Dear guests your operation system is: ' + operation_system)
    elif (operation_system == 'Linux'):
        command_result = os.system('pip list | grep ' + packages_install + '> ' + ' checkversion.txt')
        print('Dear guests your operation system is: ' + operation_system)

    # with open('checkversion.txt','w') as file:
    #     command_result = file.read()

    if command_result == packages_install:
        print(packages_install + " has been installed on this computer")
        sys.exit()
    elif command_result != packages_install:
        print("Start to setup " + packages_install + " you want to installed in this laptop")
    username = os.getlogin()
    with open("packages_log.txt", "w") as file:
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        file.write(username + " downloaded the " + packages_install + " downloaded time: " + current_time)


def install_packages(packages_install):
    mirrors_pool = {"pypi.tuna.tsinghua.edu.cn": "https://pypi.tuna.tsinghua.edu.cn/simple","pypi.douban.com": "http://pypi.douban.com/simple/","mirrors.aliyun.com": "http://mirrors.aliyun.com/pypi/simple/"}

    with open("mirrors_links.txt", "w") as file2:
        file2.write(str(mirrors_pool))
        file2.close()

    # 打印mirrors_pool 
    for key_example in mirrors_pool():
        print(key_example, mirrors_pool[key_example])


    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # CDing the functions will more powerful.Use the beautiful Algorithm to make the  program more wonderful.Learn to use dictionary.
    # time_out = ??? #
    # try:
    #     pip_install1 = os.system('pip install ' + packages_install + " -i https://pypi.tuna.tsinghua.edu.cn/simple" + ' --trusted-host ' + " pypi.tuna.tsinghua.edu.cn")
    #     response_tsing = urllib.request.urlopen('https://pypi.tuna.tsinghua.edu.cn', timeout=5)
    # except urllib.error.URLError as e:
        # if isinstance(e.reason, socket.timeout) == time_out:   # ()
        #     print('tsinghua requested timeout')
        #     # break
        #     try:
        #         pip_install2 = os.popen('pip install ' + packages_install + " -i http://pypi.douban.com/simple/" + ' --trusted-host ' + " pypi.douban.com")
        #         print('try to download the packages from' + mirrors_pool[])
    # try:
    #     pip_install2 = os.popen('pip install ' + packages_install + " -i http://pypi.douban.com/simple/" + ' --trusted-host ' + " pypi.douban.com")
    #     response_douban = urllib.request.urlopen('http://pypi.douban.com', timeout=20)
    # except urllib.error.URLError as e1:
    #     if isinstance(e1.reason, socket.timeout):
    #         print('douban requested timeout')
    # try:
    #     pip_install3 = os.system('pip install ' + packages_install + " -i http://mirrors.aliyun.com/pypi/simple/" + ' --trusted-host ' + " mirrors.aliyun.com")
    #     response_aliyun = urllib.request.urlopen('http://mirrors.aliyun.com', timeout=15)
    # except urllib.error.URLError as e2:
    #     if isinstance(e2.reason, socket.timeout):
    #         print('aliyun requested timeout')


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



