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
    tasklist = []
    lock = Lock()
    choose_task = int(input('Dear master please choose which grabber you want to use: ' + 'Only pick the number: 1.ali 2.douban 3.tsinghua 4.ustc' + '\n'))
    if choose_task == 1:
        thread1 = threading.Thread(target=installation_packages, args=('ali_spider.py',))
        thread1.start()
    elif choose_task == 2:
        thread2 = threading.Thread(target=installation_packages, args=('douban_spider.py',))
        thread2.start()
    elif choose_task == 3:
        thread3 = threading.Thread(target=installation_packages, args=('tsinghua_spider.py',))
        thread3.start()
    elif choose_task == 4:
        thread4 = threading.Thread(target=installation_packages, args=('ustc_spider.py',))
        thread4.start()
    else:
        print('Type error,please try again!!!')
