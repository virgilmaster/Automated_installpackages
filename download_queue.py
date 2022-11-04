import os
import time
import datetime
from main import read_requirements
from main import handle_packages
import platform
import threading



def current_packages():
    operation_system = platform.system()
    if operation_system == "Windows":
        pack_num = os.popen('type requirements.txt | find /v /c""')
        username = os.getlogin()
        output_num = pack_num.read()
        pack_num.close()


    elif operation_system == "Linux":
        pack_num = os.popen('cat requirements.txt | wc -l"')
        command_username = os.popen('whoami')
        username = command_username.read()
        output_num = pack_num.read()
        command_username.close()
        pack_num.close()
        


    pack_information = read_requirements("requirements.txt")
    numbers = int((output_num[0].replace("\n","")))


    
    for i in range(numbers):
        package_detail = str(pack_information[i])
        package_result = package_detail.split("'")[1].split("'")[0]
        converted_result = package_result.split(",")[0]
        
    #print(converted_result + " Plz make sure it's the correct version packages you want to installed on your computer!")



def installation_packages():
    try:
        # 暂时先这样子写: 目前阶段能跑起来就行
        # 周末打算开发出多线程 下载的方法
        os.system('python ali_spider.py')
        time.sleep(5)
        os.system('python tsinghua_spider.py')
        time.sleep(5)
        os.system('python ustc_spider.py')
        time.sleep(5)
        os.system('python douban_spider.py')
        time.sleep(5)
        
    except Exception as err:
        print(err)
        
    else:
        print("Failed to download the resource!!!")
        time.sleep(5)
        



# def check_packages():
    # Pseudocode
    # if pip list result have check the packages 
    # and break the thread spider downloading the same packages 
    # and print the final result to the guests
    # when ali_spider finished:
    # os.system() check packages
    # result == $package_name:
    # break spider
    # next package 
    # all finish pass
    

if __name__ == '__main__':
    current_packages()
    installation_packages()
    # logical desgign
    # when spider raise expection
    # jump to the next spider thread
    # thread1 = 
    # thread2 =
