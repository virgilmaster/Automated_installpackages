from jmespath import search
import requests
import os
import time
import platform



def write_mirrors():
    with open("Mirrors_links.json", "w") as mirrors_file:
        mirrors_file.write(str(mirror_pools))
        mirrors_file.close()
    print("Wait a moment,loading the settings")
    time.sleep(3)


def read_requirements1(file_name):
    pack_information = []  
    file = open(file_name,'r') 
    file_pack_information = file.readlines()
    for row in file_pack_information:  
        tmp_list = row.split(' ')
        tmp_list[-1] = tmp_list[-1].replace('\n',',')
        pack_information.append(tmp_list)
    return pack_information



def handle_packages1(pack_information):
    numbers = int(final_num) 
    for i in range(numbers):  
        package_detail = str(pack_information[i]) 
        package_result = package_detail.split("'")[1].split("'")[0]
        package_names = package_result.split("==")[0]
    return package_names


def mirrors_master(mirror_pools):
    aliyun_pool = search("aliyun", mirror_pools)
    final_ali = str(aliyun_pool)
    aliyun_domain = final_ali.split(' ')[1].replace("'", "").replace(",", "")
    aliyun_link = final_ali.split(' ')[3].replace("'", "").replace("}", "").replace("]", "")
    tsinghua_pool = search("tsinghua", mirror_pools)
    final_tsinghua = str(tsinghua_pool)
    tsinghua_domain = final_tsinghua.split(' ')[1].replace("'", "").replace(",", "")
    tsinghua_link = final_tsinghua.split(' ')[3].replace("'", "").replace("}", "").replace("]", "")
    douban_pool = search("douban", mirror_pools)
    final_douban = str(douban_pool)
    douban_domain = final_douban.split(' ')[1].replace("'", "").replace(",", "")
    douban_link = final_douban.split(' ')[3].replace("'", "").replace("}", "").replace("]", "")
    ustc_pool = search("ustc", mirror_pools)
    final_ustc = str(ustc_pool)
    ustc_domain = final_ustc.split(' ')[1].replace("'", "").replace(",", "")
    ustc_link = final_ustc.split(' ')[3].replace("'", "").replace("}", "").replace("]", "")



def ali_spider(aliyun_domain,aliyun_link,package_names):
    r_ali = requests.get("http://" + aliyun_domain)
    code_ali = r_ali.status_code
    if code_ali != 200:
        print("ali's requests is error")
        raise Exception("aliyun can not download the resources")
    else:
        print("Perpare to download the resources!!!")
        time.sleep(5)
        os.system("pip install " + package_names + " -i " + aliyun_link + " --trusted-host " + aliyun_domain)
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

def tsinghua_spider(tsinghua_domain,tsinghua_link,package_names):
    r_tsinghua = requests.get("http://" + tsinghua_domain)
    code_tsinghua = r_tsinghua.status_code
    if code_tsinghua != 200:
        print("tsinhua's requests is error")
        raise Exception("tsinghua can not download the resources")
    else:
        print("Perpare to download the resources!!!")
        time.sleep(5)
        os.system("pip install " + package_names + " -i " + tsinghua_link + " --trusted-host " + tsinghua_domain)
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

def ustc_spider(ustc_domain,ustc_link,package_names):
    r_ustc = requests.get("http://" + ustc_domain)
    code_ustc = r_ustc.status_code
    if code_ustc != 200:
        print("ustc's requests is error")
        raise Exception("ustc can not download the resources")
    else:
        print("Perpare to download the resources!!!")
        time.sleep(5)
        os.system("pip install " + package_names + " -i " + ustc_link + " --trusted-host " + ustc_domain)
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')


def douban_spider(douban_domain,douban_link,package_names):
    r_douban = requests.get("http://" + douban_domain)
    code_douban = r_douban.status_code
    if code_douban != 200:
        print("douban's requests is error")
        raise Exception("douban can not download the resources")
    else:
        print("Perpare to download the resources!!!")
        time.sleep(5)
        os.system("pip install " + package_names + " -i " + douban_link + " --trusted-host " + douban_domain)
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')


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
    write_mirrors()
    operation_system = platform.system()
    if operation_system == "Windows":
        pack_num = os.popen('type requirements.txt | find /v /c""')
        username = os.getlogin()
        output_num = pack_num.readlines()
        final_num = str(output_num[0]).replace("\n",'')
        pack_num.close()
    elif operation_system == "Linux":
        pack_num = os.popen('cat requirements.txt | wc -l"')
        command_username = os.popen('whoami')
        username = command_username.read()
        output_num = pack_num.readlines()
        final_num = str(output_num[0]).replace("\n",'')
        command_username.close()
        pack_num.close()
    read_requirements1(file_name)
    pack_information = read_requirements1(file_name)
    handle_packages1(pack_information)
    package_names = handle_packages1(pack_information)
