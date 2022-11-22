# Author: Virgil.She
# Date: 2022/11/22
# Version: 1.0.0
# Introduction: A fans of python programming language

import time,datetime
import platform
from functions.filehandler import filesdetails
from log.artist import logwriter
from functions.progessbar import timebar


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
            
            from functions.inspector import checker
            from queue.beesfly import wizard
            from threading import Lock
            import threading

        except ImportError as e:
            raise e

        domainlist = ['aliyun', 'tsinghua', 'ustc', 'douban']
        loop_num = len(domainlist)
        j = 0
        while j < loop_num:
            sourcenames = domainlist[j]
            # witch = wizard(domainlist[j])
            # witch.spellmagic()
            print(sourcenames)
            j += 1
            

    # lock = Lock()
    # tk = threading.Thread(target=handle_packages, args=(,))
    # tk.start()
