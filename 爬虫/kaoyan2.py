from bs4 import BeautifulSoup

import re
import os
import requests
import json
import time
import lxml

import OpenSSL
mainsite="http://kaoyan.eol.cn/shiti/zhuanyeke/201606/t20160601_1405411.shtml"

#得到源码
def getbs(url):
    req=requests.get(url)
    req.encoding="gbk"#这里因为1024图片帖子内的编码是gbk,如果不指明编码，得到的是乱码
    bsobj = BeautifulSoup(req.text, "lxml")
    return bsobj


def getallpage(url,pattern):
    urls = []
    bsobj = getbs(url)
    #print(bsobj)
    urls += bsobj.find_all(bsobj,pattern)
    return urls

def gettag(url,pattern,classmethod):
    bsobj = getbs(url)
    tags = bsobj.find_all(pattern,classmethod)
    return tags



urls = getallpage(mainsite,pattern=r"<a href=\"http://kaoyan.eol.cn/shiti/zhuanyeke/2016[\S]+?年</a>")
urlss = {}
