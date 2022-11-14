import os
import datetime
import logging
from main import platform
from main import datetime
from filehandler import filesdetails



def log_record(operation_system,pack_information):
    if operation_system == "Windows":
        username = os.getlogin()
        path_result = os.getcwd()
        pack_num = os.popen('type requirements.txt | find /v /c""')
        output_num = pack_num.readlines()
        final_num = str(output_num[0]).replace("\n",'')
        pack_num.close()
        c_t = str(datetime.datetime.now().strftime('%Y%m%d'))
        download_dir = path_result + '\downloadlog'
        log_path = download_dir + "download_" + c_t + ".log"

    elif operation_system == "Linux":
        path_result = os.getcwd()
        command_username = os.popen('whoami')
        username = command_username.read()
        pack_num = os.popen('cat requirements.txt | wc -l')
        output_num = pack_num.readlines()
        final_num = str(output_num[0]).replace("\n",'')
        pack_num.close()
        c_t = str(datetime.datetime.now().strftime('%Y%m%d'))
        download_dir = path_result + '/downloadlog'
        log_path = download_dir + "download_" + c_t + ".log"

    
    if not os.path.exists(download_dir):
        os.mkdir(download_dir)
        os.chdir(download_dir)
        log_builder = logging.getLogger()
        log_builder.setLevel(logging.INFO)
        current_time = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        file_hand = logging.FileHandler(filename="download_" + c_t + ".log",mode='a',encoding='utf-8')
        log_builder.addHandler(file_hand)

        numbers = int(final_num)
        j = 0
        while j < numbers: 
            package_detail = str(pack_information[j]) 
            package_result = package_detail.split("'")[1].split("'")[0]
            package_names = package_result.split("==")[0]  
            package_version = package_result.split("==")[1]
            log_builder.info((str(username) + " try to download the " + package_names + " and the version is " + package_version + " at " + current_time))
            j += 1
            
    else:
        os.chdir(download_dir)
        log_builder = logging.getLogger()
        log_builder.setLevel(logging.INFO)
        current_time = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        file_hand = logging.FileHandler(filename="download_" + c_t + ".log",mode='a',encoding='utf-8')
        log_builder.addHandler(file_hand)

        numbers = int(final_num)
        j = 0
        while j < numbers: 
            package_detail = str(pack_information[j]) 
            package_result = package_detail.split("'")[1].split("'")[0]
            package_names = package_result.split("==")[0]  
            package_version = package_result.split("==")[1]
            log_builder.info((str(username) + " try to download the " + package_names + " and the version is " + package_version + " at " + current_time))
            j += 1




if __name__ == '__main__':
    files_read = filesdetails('Windows','requirements.txt')
    pack_information = files_read.readlines
    operation_system = platform.system()
    log_record(operation_system,pack_information)
