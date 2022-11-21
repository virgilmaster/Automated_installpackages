# Author: Virgil.She
# Date: 2022/11/21
# Version: 0.2.26
# Introduction: A fans of python programming language

import time,datetime
import platform
from filehandler import filesdetails
import threading
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

def handle_packages():
    try:
        from beesfly import wizard
        from inspector import checker
        from threading import Lock
    except ImportError as e:
        raise e
    tasklist = ['aliyun','tsinghua','ustc','douban']
    loop_num = len(tasklist)
    lock = Lock()
    j = 0
    file = 'requirements.txt'
    witch = wizard(file)
    caller = witch.spellmagic
    while j < loop_num:
        tk = threading.Thread(target=caller, args=(tasklist[j],))
        tk.start()
        lock.acquire()
        j += 1

if __name__ == "__main__":
    start_counter = time.perf_counter()
    os_result = platform.system()
    print("Begin time is: " + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    files_read = filesdetails(str(os_result),'requirements.txt')
    operation_system = platform.system()
    pack_information = files_read.readinfo
    check_system(operation_system)
    handle_packages()
    launcher = logwriter(operation_system,pack_information)
    launcher.log_record()
    print("End time is: " + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    end_counter = time.perf_counter()
    runtime = timebar(start_counter,end_counter)
    runtime.counter_process()
