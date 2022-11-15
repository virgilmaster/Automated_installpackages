from filehandler import filesdetails
from sourceholder import mirrors
from collector import spiders
import threading
import time
from multiprocessing import Process,Lock
from queue import Queue


# files2 = filesdetails('Windows','requirements.txt')
# print(files2.counter)
# print(files2.readinfo)

# ali_result = mirrors('aliyun')
# print(ali_result.mirrorspools)

def runner(y):
    try:
        collect_name = spiders(y)
        collect_name.downloader()

    except Exception as err:
        print(err)

    else:
        print("Failed to download the resource!!!")
        time.sleep(5)

if __name__ == '__main__':
    task_name = ['aliyun','tsinghua','ustc','douban']
    loop_num = len(task_name)
    lock = Lock()
    j = 0
    while j < loop_num:
        tk = threading.Thread(target=runner, args=(task_name[j],))
        #tk.setDaemon(True)
        tk.start()
        #tk.join()
        time.sleep(10)
        j += 1
