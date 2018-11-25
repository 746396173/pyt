# coding=utf-8
#www5.javfinder.is
'''
起始页 https://www5.javfinder.is/movie/hot.html

'''
from bs4 import BeautifulSoup
import re
import os
import requests
import json
import time
import lxml
import OpenSSL
from selenium import webdriver


mainsite = "http://www5.javfinder.is"
def getbs(url):#获取页面源代码
    req = requests.get(url).text
    bsobj = BeautifulSoup(req, "lxml")
    return bsobj

def clerurl(bsobj):
    div = []
    div += bsobj.find_all("a",title = True,href=re.compile(r"^/movie.*"))
    div = [mainsite+i['href'] for i in div]
    return div
'https://www5.javfinder.is/movie/cherries-chrv-023-kujyo-sayaka-big-boobs-are-too-big-for-a-cabin-attendant-who-is-not-able-to-stand-straight-the-manager-will-be-forced-to-reinspan-the-bmi.html'

def clerurll (url):#
    bsobj = getbs(url)
    div = bsobj.find_all("div",)#动态页面,所以匹配不到目标
    print(div)
    return div

url = "http://www5.javfinder.is/movie/hot.html"
bs = getbs(url)
#print(bs)
div = clerurl(bs)
print('------------'+ str(div) +"---------------------")

dizhi = []
for url in  div:
    print(url)
    dizhi = clerurll(url)
    time.sleep(2)
    print(dizhi)
print(dizhi)
