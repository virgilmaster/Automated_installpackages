import os
import time
import datetime
import jmespath
from jmespath import search
from automation_upgrade import read_requirements
from automation_upgrade import handle_packages
import platform

# Json data from dictionary
def installation_mirrors(mirror_pools):
    with open("Mirrors_links.json", "w") as mirrors_file:
        mirrors_file.write(str(mirror_pools))
        mirrors_file.close()
    print("Wait a moment,loading the settings")

def check_packages():
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
    numbers = int(output_num)
    for i in range(numbers):
        package_detail = str(pack_information[i])
        package_result = package_detail.split("'")[1].split("'")[0]
        converted_result = package_result.split(",")[0]
        package_names = package_result.split("==")[0]
        package_version = package_result.split("==")[1]
        print(converted_result)

    aliyun_data = search("aliyun",mirror_pools)
    final_ali = str(aliyun_data)
    aliyun_domain = final_ali.split(' ')[1].replace("'","").replace(",","")
    aliyun_link = final_ali.split(' ')[3].replace("'","").replace("}","").replace("]","")
    try:
        os.system("pip install " + converted_result + "-i" + " " + aliyun_link + " --trusted-host " + aliyun_domain)
    except Exception as e:
        print(e)

    tsinghua_data = search("tsinghua",mirror_pools)
    final_tsinghua = str(tsinghua_data)
    tsinghua_domain = final_tsinghua.split(' ')[1].replace("'","").replace(",","")
    tsinghua_link = final_tsinghua.split(' ')[3].replace("'","").replace("}","").replace("]","")
    try:
        os.system("pip install " + converted_result + "-i" + " " + tsinghua_link + " --trusted-host " + tsinghua_domain)
    except Exception as e:
        print(e)

    douban_data = search("douban",mirror_pools)
    final_douban = str(douban_data)
    douban_domain = final_douban.split(' ')[1].replace("'","").replace(",","")
    douban_link = final_douban.split(' ')[3].replace("'","").replace("}","").replace("]","")
    try:
        os.system("pip install " + converted_result + "-i" + " " + douban_link + " --trusted-host " + douban_domain)
    except Exception as e:
        print(e)

    ustc_data = search("ustc",mirror_pools)
    final_ustc = str(ustc_data)
    ustc_domain = final_ustc.split(' ')[1].replace("'","").replace(",","")
    ustc_link = final_ustc.split(' ')[3].replace("'","").replace("}","").replace("]","")
    try:
        os.system("pip install " + converted_result + "-i" + " " + ustc_link + " --trusted-host " + ustc_domain)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    mirror_pools = {"aliyun": [
    {"domain": "mirrors.aliyun.com","link":"http://mirrors.aliyun.com/pypi/simple/"}],
    "ustc":[
    {"domain":"pypi.mirrors.ustc.edu.cn","link": "https://pypi.mirrors.ustc.edu.cn/simple/"}],
    "douban":[
    {"domain":"pypi.douban.com","link": "http://pypi.douban.com/simple/"}],
    "tsinghua":[
    {"domain":"pypi.tuna.tsinghua.edu.cn","link": "https://pypi.tuna.tsinghua.edu.cn/simple/"}]
    }
    check_packages()
    installation_mirrors(mirror_pools)

