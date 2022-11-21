# Author: Virgil.She
# Date: 2022/11/21
# Version: 0.2.5
# Introduction: A fans of python programming language

import time,datetime
import platform
from filehandler import filesdetails
from artist import logwriter
from progessbar import timebar


class runner:
    def __init__(self,opsys,filename):
        self.opsys = opsys
        self.filename = filename

    def check_system(self):
        os_result = self.opsys
        print('Dear guests,begin to check your system: ')
        counter1 = 0
        while counter1 < 6:
            time.sleep(1)
            print('{:=^89}'.format("Checking"))
            counter1 += 1
        time.sleep(1)
        print('Your system is: ' + os_result + '...')


    def handle_packages(self):
        try:
            from beesfly import wizard
            from inspector import checker
            from threading import Lock
            import threading
        except ImportError as e:
            raise e
        tasklist = ['aliyun', 'tsinghua', 'ustc', 'douban']
        loop_num = len(tasklist)
        j = 0
        while j < loop_num:
            sourcenames = tasklist[j]
            witch = wizard(sourcenames)
            witch.spellmagic
            j += 1

if __name__ == "__main__":
    start_counter = time.perf_counter()
    file = 'requirements.txt'
    os_result = platform.system()
    check_system(os_result)
    print("Begin time is: " + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    files_read = filesdetails(file)
    pack_information = files_read.readinfo
    # lock = Lock()
    # tk = threading.Thread(target=handle_packages, args=(,))
    # tk.start()
    launcher = logwriter(pack_information)
    launcher.log_record()
    handle_packages()
    print("End time is: " + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    end_counter = time.perf_counter()
    runtime = timebar(start_counter,end_counter)
    runtime.counter_process()
