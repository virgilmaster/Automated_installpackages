import os 
import requests
from jmespath import search
import time
import platform



def read_requirements1(file_name):
    pack_information = []  
    file = open(file_name,'r') 
    file_pack_information = file.readlines()
    for row in file_pack_information:  
        tmp_list = row.split(' ')
        tmp_list[-1] = tmp_list[-1].replace('\n',',')
        pack_information.append(tmp_list)
    return pack_information


def ustc_downloader(pack_information):
    operation_system = platform.system()
    if operation_system == "Windows":
        pack_num = os.popen('type requirements.txt | find /v /c""')
        output_num = pack_num.readlines()
        final_num = str(output_num[0]).replace("\n",'')
        pack_num.close()
    elif operation_system == "Linux":
        pack_num = os.popen('cat requirements.txt | wc -l"')
        command_username = os.popen('whoami')
        output_num = pack_num.readlines()
        final_num = str(output_num[0]).replace("\n",'')
        command_username.close()
        pack_num.close()
    numbers = int(final_num)
    for i in range(numbers):
        package_detail = str(pack_information[i])
        package_result = package_detail.split("'")[1].split("'")[0]
        ustc_pool = search("ustc", mirror_pools)
        final_ustc = str(ustc_pool)
        ustc_domain = final_ustc.split(' ')[1].replace("'", "").replace(",", "")
        ustc_link = final_ustc.split(' ')[3].replace("'", "").replace("}", "").replace("]", "")
        r_ustc = requests.get("http://" + ustc_domain)
        code_ustc = r_ustc.status_code
        if code_ustc != 200:
            print("ustc's requests is error")
            raise Exception("aliyun can not download the resources")
        else:
            print("Perpare to download the resources!!!")
            time.sleep(5)
            begin_time = time.time()
            os.system("pip install " + package_result.replace(",","") + " -i " + ustc_link + " --trusted-host " + ustc_domain)
            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            end_time  = time.time()
            print("The total time is: %s" % (end_time - begin_time))

if __name__ == '__main__':
    file_name = 'requirements.txt'
    mirror_pools = {"aliyun": [
    {"domain": "mirrors.aliyun.com","link":"http://mirrors.aliyun.com/pypi/simple/"}],
    "ustc":[
    {"domain":"pypi.mirrors.ustc.edu.cn","link": "https://pypi.mirrors.ustc.edu.cn/simple/"}],
    "douban":[
    {"domain":"pypi.douban.com","link": "http://pypi.douban.com/simple/"}],
    "tsinghua":[
    {"domain":"pypi.tuna.tsinghua.edu.cn","link": "https://pypi.tuna.tsinghua.edu.cn/simple/"}]
    }
    read_requirements1(file_name)
    pack_information = read_requirements1(file_name)
    ustc_downloader(pack_information)
