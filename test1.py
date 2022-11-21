# handler
from filehandler import filesdetails
# mirror master
from sourceholder import mirrors
# downloader
from collector import spiders
import threading
import time
from multiprocessing import Process,Lock
from queue import Queue
from inspector import checker

files2 = filesdetails('Windows','requirements.txt')
# print(files2.counter)
# print(files2.readinfo)
# print(files2.versionfilter)
# print(files2.namefilter)
namelist = files2.namefilter
versionlist = files2.versionfilter
# print(namelist)
# print(versionlist)

# import platform
# os = platform.system()
# file = 'requirements.txt'
# files3 = checker(str(os),file)
# print(files3.versioncheck)

from beesfly import wizard
from inspector import checker
import os
os_result = os.system()
file_name = 'requirements.txt'
task1 =  checker(os_result,file_name)
uninstall = task1.versioncheck
print(uninstall)

# ali_result = mirrors('aliyun')
# print(ali_result.mirrorspools)

# def runner(y):
#     try:
#         collect_name = spiders(y)
#         collect_name.downloader()

#     except Exception as err:
#         print(err)

#     else:
#         print("Failed to download the resource!!!")
#         time.sleep(5)

# if __name__ == '__main__':
#     task_name = ['aliyun','tsinghua','ustc','douban']
#     loop_num = len(task_name)
#     lock = Lock()
#     j = 0
#     while j < loop_num:
#         tk = threading.Thread(target=runner, args=(task_name[j],))
#         #tk.setDaemon(True)
#         tk.start()
#         #tk.join()
#         time.sleep(10)
#         j += 1
