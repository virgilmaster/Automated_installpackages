import os
import time
from multiprocessing import Process,Lock
import threading
from queue import Queue
from collector import spiders



def installation_packages(x):
    try:
        collect_name = spiders(x)
        collect_name.downloader()

    except Exception as error:
        print(error)

    else:
        print("Failed to download the resource!!!")
        time.sleep(5)



if __name__ == '__main__':
    tasklist = ['aliyun','tsinghua','ustc','douban']
    loop_num = len(tasklist)
    lock = Lock()
    j = 0
    while j < loop_num:
        tk = threading.Thread(target=installation_packages, args=(tasklist[j],))
        #tk.setDaemon(True)
        tk.start()
        #tk.join()
        time.sleep(10)
        j += 1
