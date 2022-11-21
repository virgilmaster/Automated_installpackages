# Author: Virgil.She
# Date: 2022/11/21
# Version: 0.2.28
# Introduction: A fans of python programming language

import time,datetime
import platform
from filehandler import filesdetails
import threading
from artist import logwriter
from progessbar import timebar
from threading import Lock


def check_system(operation_system):
    print('Dear guests,begin to check your system: ')    
    counter1 = 0 
    while counter1 < 6:
        time.sleep(1)
        print('{:=^89}'.format("Checking"))
        counter1 += 1
    time.sleep(1)
    print('Your system is: ' + operation_system + '...')

def handle_packages(x):
    try:
        from beesfly import wizard
        from inspector import checker
        from threading import Lock
    except ImportError as e:
        raise e

    witch = wizard(x)
    caller = witch.spellmagic
    lock = Lock()


if __name__ == "__main__":
    start_counter = time.perf_counter()
    os_result = platform.system()
    print("Begin time is: " + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    files_read = filesdetails(str(os_result),'requirements.txt')
    operation_system = platform.system()
    pack_information = files_read.readinfo
    check_system(operation_system)
    tasklist = ['aliyun','tsinghua','ustc','douban']
    loop_num = len(tasklist)
    lock = Lock()
    j = 0
    file = 'requirements.txt'
    while j < loop_num:
        tk = threading.Thread(target=handle_packages, args=(tasklist[j],))
        tk.start()
        lock.acquire()
        j += 1
    launcher = logwriter(operation_system,pack_information)
    launcher.log_record()
    print("End time is: " + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    end_counter = time.perf_counter()
    runtime = timebar(start_counter,end_counter)
    runtime.counter_process()
