# Author: Virgil.She
# Date: 2022/11/16
# Version: 0.2.18
# Introduction: A fans of python programming language

import os
import re,string
import time
import datetime
import platform
from filehandler import filesdetails



def check_system():
    print('Dear guests,begin to check your system: ')    
    counter1 = 0 
    while counter1 < 6:
        time.sleep(1)
        print('{:=^89}'.format("Checking"))
        counter1 += 1
    time.sleep(1)
    print('Your system is: ' + operation_system + '...')

def handle_packages(pack_information):
    final_num = files_read.counter
    numbers = int(final_num)  
    for i in range(numbers):  
        package_detail = str(pack_information[i]) 
        package_result = package_detail.split("'")[1].split("'")[0]
        converted_result = package_result.split(",")[0]
        package_names = package_result.split("==")[0]  
        package_version = package_result.split("==")[1]
        final_version = re.sub('[%s]' % re.escape(string.punctuation), '', package_version)

        
        if operation_system == "Windows":
            packages_installed = os.popen("pip list | findstr " + package_names) 
            result_installed = packages_installed.readlines()     
            packages_installed.close()                              
            installed_version = str(result_installed).split(" ")[-1]
            final_installed = (re.sub('[%s]' % re.escape(string.punctuation), '', installed_version)).replace("n","")
            print('{:=^89}'.format("Line"))
            try:
                from artist import logwriter
                launcher = logwriter(operation_system,pack_information)
                launcher.log_record()
            except Warning as e:
                print(e,'Something wrong with the module')

            if installed_version == '[]':
                print(package_names +  " have not be installed")
                print("Start launch the webspiders,to download the new " + package_names)
                
                #os.system("python download_queue.py")
            elif final_installed == final_version:
                print("The " + package_names + " is in the same version,no necessary to install " + package_names + " again")

            else:
                print("The packages's version is " + installed_version)
                print("Start to change " + package_names + "'s version,plz wait a moment~.~")
                # os.system("pip uninstall" + " " + package_names)
                
                #os.system("python download_queue.py")
        

        elif operation_system == "Linux":
            os.system('alias python=' + 'python3')
            packages_installed = os.popen("pip list | grep " + package_names) 
            result_installed = packages_installed.readlines()     
            packages_installed.close()
            installed_version = str(result_installed).split(" ")[-1]
            final_installed = (re.sub('[%s]' % re.escape(string.punctuation), '', installed_version)).replace("n","")
            print('{:=^89}'.format("Line"))
            try:
                from artist import logwriter
                launcher = logwriter(operation_system,pack_information)
                launcher.log_record()
            except Warning as e:
                print(e,'Something wrong with the module')
           
            if installed_version == '[]':
                print(package_names +  " have not be installed")
                print("Start launch the webspiders,to download the new " + package_names)
                #os.system("python download_queue.py")
            elif final_installed == final_version:
                print("The " + package_names + " is in the same version,no necessary to install " + package_names + " again")
            else:
                print("The packages's version is " + installed_version)
                print("Start to change" + package_names + "'s version,plz wait a moment~.~")
                #os.system("pip uninstall" + " " + package_names)
                #os.system("python download_queue.py")


def counter_process(runtime):
    scale = 100
    print('{:=^89}'.format("Line"))
    print("Start downloading the python packages".center(scale // 2, "-"))
    for i in range(scale + 1):
        conuter1 = ">" * i
        counter2 = "-" * (scale - i)
        counter3 = (i / scale) * 100
        print("\r{:^3.0f}%[{}>{}]{:.2f}s".format(counter3, conuter1, counter2, runtime), end="")
        time.sleep(0.1)
    print("\n" + "All the job is done,lucky so much".center(scale // 2, "-"))


if __name__ == "__main__":
    start_counter = time.perf_counter()
    os_result = platform.system()
    print("Begin time is: " + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    files_read = filesdetails(str(os_result),'requirements.txt')
    operation_system = platform.system()
    pack_information = files_read.readinfo
    check_system()
    handle_packages(pack_information)
    print("End time is: " + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    end_counter = time.perf_counter()
    runtime = end_counter - start_counter
    counter_process(runtime)
