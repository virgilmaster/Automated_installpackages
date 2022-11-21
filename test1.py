'''
This is a test function files.
It shows how i learn the python programming step by step.
'''
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

# files2 = filesdetails('Windows','requirements.txt')
# # print(files2.counter)
# # print(files2.readinfo)
# # print(files2.versionfilter)
# # print(files2.namefilter)
# namelist = files2.namefilter
# versionlist = files2.versionfilter
# print(namelist)
# print(versionlist)


files = filesdetails('Windows','requirements.txt')
files33 = files.readinfo
for i in range(len(files33)):
    #print(files33[i])
    #print(type(files33[i]))
    print(str(files33[i]).split(',')[0].replace("['",''))
# import platform
# os = platform.system()
# file = 'requirements.txt'
# files3 = checker(str(os),file)
# print(files3.versioncheck)

# from beesfly import wizard
# from inspector import checker
# import os
# os_result = os.system()
# file_name = 'requirements.txt'
# task1 =  checker(os_result,file_name)
# uninstall = task1.versioncheck
# print(uninstall)

# ali_result = mirrors('aliyun')
# print(ali_result.mirrorspools)

