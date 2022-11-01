from jmespath import search
import requests
import os


def get_result(mirror_pools):
    with open("Mirrors_links.json", "w") as mirrors_file:
        mirrors_file.write(str(mirror_pools))
        mirrors_file.close()
    print("Wait a moment,loading the settings")

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


    r_ali = requests.get("http://" + aliyun_domain)
    r_tsinghua = requests.get("http://" + tsinghua_domain)
    r_douban = requests.get("http://" + douban_domain)
    r_ustc = requests.get("http://" + ustc_domain)

    code_ali = r_ali.status_code
    code_tsinghua = r_tsinghua.status_code
    code_douban = r_douban.status_code
    code_ustc = r_ustc.status_code

    print(code_ali)
    print(code_tsinghua)
    print(code_douban)
    print(code_ustc)

    if code_ali != 200:
        raise Exception("aliyun can not download the resources")
    elif code_tsinghua != 200:
        raise Exception("tsinghua can not download the resources")
    elif code_douban != 200:
        raise Exception("douban can not download the resources")
    elif code_ustc != 200:
        raise Exception("ustc can not download the resources")

    try:
        os

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
    get_result(mirror_pools)
