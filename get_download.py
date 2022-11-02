from jmespath import search
import requests
import os
import threading
import winproxy

def write_mirrors():
    with open("Mirrors_links.json", "w") as mirrors_file:
        mirrors_file.write(str(mirror_pools))
        mirrors_file.close()
    print("Wait a moment,loading the settings")

def ali_spider(aliyun_domain):
    r_ali = requests.get("http://" + aliyun_domain)
    code_ali = r_ali.status_code
    if code_ali != 200:
        print("ali's requests is error")
        #raise Exception("aliyun can not download the resources")
    else:
        print("Perpare to download the resources!!!")

def tsinghua_spider(tsinghua_domain):
    r_tsinghua = requests.get("http://" + tsinghua_domain)
    code_tsinghua = r_tsinghua.status_code
    if code_tsinghua != 200:
        print("tsinhua's requests is error")
        #raise Exception("tsinghua can not download the resources")
    else:
        print("Perpare to download the resources!!!")

def ustc_spider(ustc_domain):
    r_ustc = requests.get("http://" + ustc_domain)
    code_ustc = r_ustc.status_code
    if code_ustc != 200:
        print("ustc's requests is error")
        #raise Exception("ustc can not download the resources")
    else:
        print("Perpare to download the resources!!!")

def douban_spider(douban_domain):
    r_douban = requests.get("http://" + douban_domain)
    code_douban = r_douban.status_code
    if code_douban != 200:
        print("douban's requests is error")
        #raise Exception("douban can not download the resources")
    else:
        print("Perpare to download the resources!!!")



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
    write_mirrors()
    task_ali = threading.Thread(target=ali_spider,args=aliyun_domain)
    task_tsinghua = threading.Thread(target=tsinghua_spider,args=tsinghua_domain)
    task_ustc = threading.Thread(target=ustc_spider,args=ustc_domain)
    task_douban = threading.Thread(target=douban_spider,args=douban_domain)
