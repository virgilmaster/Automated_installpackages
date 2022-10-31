import os
import time
import datetime
import jmespath
from jmespath import search
import urllib3
import requests
import re

# Json data from dictionary
def installation_mirrors():
    mirror_pools = {"aliyun": [
    {"domain": "mirrors.aliyun.com","link":"http://mirrors.aliyun.com/pypi/simple/"}],
    "ustc":[
    {"domain":"pypi.mirrors.ustc.edu.cn","link": "https://pypi.mirrors.ustc.edu.cn/simple/"}],
    "douban":[
    {"domain":"pypi.douban.com","link": "http://pypi.douban.com/simple/"}],
    "tsinghua":[
    {"domain":"pypi.tuna.tsinghua.edu.cn","link": "https://pypi.tuna.tsinghua.edu.cn/simple/"}]
    }
    print("Start downloading the packages from internet")
    aliyun_data = search("aliyun",mirror_pools)
    final_ali = str(aliyun_data)
    aliyun_domain = final_ali.split(' ')[1]
    aliyun_link = final_ali.split(' ')[3]
    print(aliyun_domain)
    print(aliyun_link)
    # ustc_data = search("ustc",mirror_pools)
    # print(ustc_data)
    # douban_data = search("douban",mirror_pools)
    # print(douban_data)
    # tsinghua_data = search("tsinghua",mirror_pools)
    # print(tsinghua_data)

# def aliyun_download():
#     try:
#         os.system("pip install" + " " + "-i" + " " + "$links" + "--trusted-host" + "$domain")
#     except
# def tsinghua_download():
#     try:
#         os.system("pip install" + " " + "-i" + " " + "$links" + "--trusted-host" + "$domain")
#     except
# def douban_download():
#     try:
#         os.system("pip install" + " " + "-i" + " " + "$links" + "--trusted-host" + "$domain")
#     except
# def ustc_download():
#     try:
#         os.system("pip install" + " " + "-i" + " " + "$links" + "--trusted-host" + "$domain")
#     except

if __name__ == '__main__':
    installation_mirrors()
    # aliyun_download()
    # tsinghua_download()
    # douban_download()
    # ustc_download()