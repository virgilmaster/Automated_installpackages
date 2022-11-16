import time
from multiprocessing import Process,Lock
import threading
from queue import Queue
from collector import spiders


class wizard():
    def __init__(self,packagename):
        self.packagename = packagename

    def spellmagic(self,x):
        try:
            from collector import spiders
        except ImportError as error:
            print(error,'Your module have been wrong plz download from github')
        uninstall_pack = self.packagename
        butterfly = spiders()
        butterfly.downloader()



        # try:
        #     collect_name = spiders(x)
        #     collect_name.downloader()

        # except Exception as error:
        #     print(error)

        # else:
        #     print("Failed to download the resource!!!")
        #     time.sleep(5)



if __name__ == '__main__':
    tasklist = ['aliyun','tsinghua','ustc','douban']
    loop_num = len(tasklist)
    lock = Lock()
    j = 0
    witch = wizard()
    while j < loop_num:
        tk = threading.Thread(target=, args=(tasklist[j],))
        #tk.setDaemon(True)
        tk.start()
        #tk.join()
        time.sleep(10)
        j += 1
