'''
This is a test function files.
It shows how i learn the python programming step by step.
'''
# handler
import platform
from log.artist import logwriter
from functions.filehandler import filesdetails
# mirror master
from source.sourceholder import mirrors
# downloader
from download.collector import spiders
import threading
import time,datetime
from multiprocessing import Process,Lock
from queue import Queue
from functions.inspector import checker
from main import runner
from functions.progessbar import timebar

# run main function
start_counter = time.perf_counter()
filename = r'C:\XXX\XXX\XXX\XXX\XXX\requirements.txt'
osys = platform.system()
run = runner(osys,filename)
run.check_system()
print("Begin time is: " + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
files_read = filesdetails(filename)
pack_information = files_read.readinfo
launcher = logwriter(filename,pack_information)
launcher.log_record()
# run.handle_packages()
end_counter = time.perf_counter()
runtime = timebar(start_counter, end_counter)
runtime.counter_process()





# run filehandler function
# files2 = filesdetails('requirements.txt')
# print(type(files2.counter))
# print(files2.readinfo)
# print(files2.versionfilter)
# print(files2.namefilter)
# namelist = files2.namefilter
# versionlist = files2.versionfilter
# print(namelist)
# print(versionlist)




# run readinfo function
# files = filesdetails('requirements.txt')
# files33 = files.readinfo
# for i in range(len(files33)):
#     #print(files33[i])
#     #print(type(files33[i]))
#     print(str(files33[i]).split(',')[0].replace("['",''))




# run inspector function
# import platform
# os = platform.system()
# file = 'requirements.txt'
# files3 = checker(file)
# files3.versioncheck



# run wizard function
# from beesfly import wizard
# from inspector import checker
# import os
# os_result = os.system()
# file_name = 'requirements.txt'
# task1 =  checker(os_result,file_name)
# uninstall = task1.versioncheck
# print(uninstall)




# run sourceholder function
# tasklist = ['aliyun','tsinghua','ustc','douban']
# j = 0
# loop_num = len(tasklist)
# while j < loop_num:
#     result = mirrors(tasklist[j])
#     print(result.mirrorspools)
#     j += 1
