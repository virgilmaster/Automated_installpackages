import os
import time
import datetime
from main import read_requirements
from main import handle_packages
import platform
from multiprocessing import Process,Lock
import threading



def current_packages():
    operation_system = platform.system()
    if operation_system == "Windows":
        pack_num = os.popen('type requirements.txt | find /v /c""')
        output_num = pack_num.read()
        pack_num.close()

    elif operation_system == "Linux":
        pack_num = os.popen('cat requirements.txt | wc -l"')
        command_username = os.popen('whoami')
        output_num = pack_num.read()
        command_username.close()
        pack_num.close()

    pack_information = read_requirements("requirements.txt")
    numbers = int((output_num[0].replace("\n","")))

    for i in range(numbers):
        package_detail = str(pack_information[i])
        package_result = package_detail.split("'")[1].split("'")[0]

def alitask():
    os.system('python' + " " + 'ali_spider.py')

def doubantask():
    os.system('python' + " " + 'douban_spider.py')

def tsinghuatask():
    os.system('python' + " " + 'tsinghua_spider.py')

def ustctask():
    os.system('python' + " " + 'ustc_spider.py')

def installation_packages(choose_task):
    try:
        final_task = choose_task
        # alitask()
        # doubantask()
        # tsinghuatask()
        # ustctask()

    except Exception as err:
        print(err)

    else:
        print("Failed to download the resource!!!")
        time.sleep(5)



if __name__ == '__main__':
    tasklist = []
    lock = Lock()
    choose_task = str(input('Dear master please choose which spider you want to use: ' + '1:ali、2:douban、3:tsinghua、4:ustc' + '\n'))
    current_packages()
    installation_packages()
    # thread1 = 
    # thread2 =
    # thread3 =
    # thread4 =
