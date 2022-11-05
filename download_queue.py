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

# def installation_packages(choose_task):
#     try:
#         if choose_task == "1":
#             alitask()
#         elif choose_task == "2":
#             doubantask()
#         elif choose_task == "3":
#             tsinghuatask()
#         elif choose_task == "4":
#             ustctask()

        #final_task = choose_task

def installation_packages():
    try:
        alitask()
        doubantask()
        tsinghuatask()
        ustctask()

    except Exception as err:
        print(err)

    else:
        print("Failed to download the resource!!!")
        time.sleep(5)



if __name__ == '__main__':
    tasklist = []
    lock = Lock()
    #choose_task = int(input('Dear master please choose which grabber you want to use: ' + 'Only pick the number: 1.ali 2.douban 3.tsinghua 4.ustc' + '\n'))
    # current_packages()
    installation_packages()
    # logical desgign
    # when spider raise expection
    # jump to the next spider thread
    # thread1 = 
    # thread2 =
    # thread3 =
    # thread4 =
