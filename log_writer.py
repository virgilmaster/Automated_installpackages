import os
import datetime
import logging
from main import platform
from main import datetime




def read_requirements2(file_name):
    pack_information = []  
    file = open(file_name,'r') 
    file_pack_information = file.readlines()
    for row in file_pack_information:  
        tmp_list = row.split(' ')
        tmp_list[-1] = tmp_list[-1].replace('\n',',')
        pack_information.append(tmp_list)
    return pack_information



def log_record(operation_system,pack_information):
    if operation_system == "Windows":
        username = os.getlogin()
        path_result = os.getcwd()
        c_t = str(datetime.datetime.now().strftime('%Y%m%d'))
        download_dir = path_result + '\downloadlog'
        log_path = download_dir + "download_" + c_t + ".log"
    elif operation_system == "Linux":
        path_result = os.getcwd()
        command_username = os.popen('whoami')
        username = command_username.read()
        c_t = str(datetime.datetime.now().strftime('%Y%m%d'))
        download_dir = path_result + '/downloadlog'
        log_path = download_dir + "download_" + c_t + ".log"

    if not os.path.exists(download_dir):
        os.mkdir(download_dir)
        if not os.path.exists(log_path):
            os.chdir(download_dir)
            print(pack_information)
            current_time = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
            log_builder = logging.getLogger()
            log_builder.setLevel(logging.INFO)
            file_hand = logging.FileHandler(filename="download_" + c_t + ".log",mode='a',encoding='utf-8')
            #stream_hand = logging.StreamHandler()
            log_format = logging.Formatter("[%(asctime)s]-[%(levelname)s]-[%(pathname)s]-[Line:%(lineno)d]-[LoggerInfo:%(message)s]")
            #log_format(fmt=log_format)
            log_builder.addHandler(file_hand)
            log_builder.info((str(username) + " try to downloading the " + str(pack_information) + " at " + current_time))
            
            
    


if __name__ == '__main__':
    file_name = 'requirements.txt'
    operation_system = platform.system()
    pack_information = read_requirements2(file_name)
    log_record(operation_system,pack_information)