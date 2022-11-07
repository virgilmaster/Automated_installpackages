import os
import time
from multiprocessing import Process,Lock
import threading
from queue import Queue




def installation_packages(x):
    try:
        os.system('python' + " " + x)

    except Exception as err:
        print(err)

    else:
        print("Failed to download the resource!!!")
        time.sleep(5)



if __name__ == '__main__':
    tasklist = ['ali_spider.py','douban_spider.py','tsinghua_spider.py','ustc_spider.py']
    loop_num = len(tasklist)
    lock = Lock()
    j = 0
    while j < loop_num:
        tk = threading.Thread(target=installation_packages, args=(tasklist[j],))
        tk.setDaemon(True)
        tk.start()
        time.sleep(10)
        j += 1
