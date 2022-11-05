import os
import time
from main import read_requirements
from main import handle_packages
from multiprocessing import Process,Lock
import threading
from queue import Queue


# def alitask():
#     os.system('python' + " " + 'ali_spider.py')

# def doubantask():
#     os.system('python' + " " + 'douban_spider.py')

# def tsinghuatask():
#     os.system('python' + " " + 'tsinghua_spider.py')

# def ustctask():
#     os.system('python' + " " + 'ustc_spider.py')


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
    #choose_task = int(input('Dear master please choose which grabber you want to use: ' + 'Only pick the number: 1.ali 2.douban 3.tsinghua 4.ustc' + '\n'))
    thread1 = threading.Thread(target=installation_packages, args=('ali_spider.py',))
    thread2 = threading.Thread(target=installation_packages, args=('douban_spider.py',))
    thread3 = threading.Thread(target=installation_packages, args=('tsinghua_spider.py',))
    thread4 = threading.Thread(target=installation_packages, args=('ustc_spider.py',))
    thread1.start()
    time.sleep(5)
    thread2.start()
    time.sleep(5)
    thread3.start()
    time.sleep(5)
    thread4.start()
    time.sleep(5)
