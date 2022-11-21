import time
from multiprocessing import Process,Lock
import threading
from queue import Queue
from collector import spiders


class wizard():
    def __init__(self,filename):
        self.filename = filename

    def spellmagic(self,x):
        try:
            from collector import spiders
            from inspector import checker
            import os 
        except ImportError as error:
            raise error
        file_name = self.filename
        os_result = os.system()
        checker_pack = checker(os_result,file_name)
        uninstall_pack = checker_pack.versioncheck
        try:
            for j in range(len(uninstall_pack)):
                final_uninstall = uninstall_pack[j]
                butterfly = spiders(x,final_uninstall)
                butterfly.downloader()
        except Exception as err:
            raise err
        else:
            print('Resources download fail')
            time.sleep(3)


if __name__ == '__main__':
    tasklist = ['aliyun','tsinghua','ustc','douban']
    loop_num = len(tasklist)
    lock = Lock()
    j = 0
    file = 'requirements.txt'
    witch = wizard(file)
    caller = witch.spellmagic
    while j < loop_num:
        tk = threading.Thread(target=caller, args=(tasklist[j],))
        #tk.setDaemon(True)
        tk.start()
        #tk.join()
        time.sleep(10)
        j += 1
