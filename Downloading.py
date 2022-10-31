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
    aliyun_domain = final_ali.split(' ')[1].replace("'","").replace(",","")
    aliyun_link = final_ali.split(' ')[3].replace("'","").replace("}","").replace("]","")
    
    ustc_data = search("ustc",mirror_pools)
    ustc_domain = final_ali.split(' ')[1].replace("'","").replace(",","")
    ustc_link = final_ali.split(' ')[3].replace("'","").replace("}","").replace("]","")
    print(ustc_domain)
    print(ustc_link)
    douban_data = search("douban",mirror_pools)
    douban_domain = final_ali.split(' ')[1].replace("'","").replace(",","")
    douban_link = final_ali.split(' ')[3].replace("'","").replace("}","").replace("]","")
    print(douban_domain)
    print(douban_link)
    tsinghua_data = search("tsinghua",mirror_pools)
    tsinghua_domain = final_ali.split(' ')[1].replace("'","").replace(",","")
    tsinghua_link = final_ali.split(' ')[3].replace("'","").replace("}","").replace("]","")
    print(tsinghua_domain)
    print(tsinghua_link)



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


#!/usr/bin/env python3
# -*- coding:utf-8 -*-
 
# def boxPrint(symbol, width, height):
#     if len(symbol) != 1:
#         raise Exception("Symbol must be a single character string.")
#     if width <= 2:
#         raise Exception("Width must be greater than 2.")
#     if height <= 2:
#         raise Exception("Height must be greater than 2.")
 
#     print(symbol * width)
#     for i in range(height - 2):
#         print(symbol + (' ' * (width - 2)) + symbol)
#     print(symbol * width)
 
 
# for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
#     try:
#         boxPrint(sym, w, h)
#     except Exception as err:
#         print('An exception happened: ' + str(err))


if __name__ == '__main__':
    installation_mirrors()
    # aliyun_download()
    # tsinghua_download()
    # douban_download()
    # ustc_download()
