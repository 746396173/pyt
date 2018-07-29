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
    bsobj = str(getbs(url))
    #print(bsobj)
    urls += re.findall(pattern,bsobj)
    return urls

def gettag(url,pattern,classmethod):
    bsobj = getbs(url)
    tags = bsobj.find_all(pattern,classmethod)
    return tags



urls = getallpage(mainsite,pattern=r"<a href=\"http://kaoyan.eol.cn/shiti/zhuanyeke/2016[\S]+?年</a>")
urlss = {}

for i in urls:
    i = re.sub(r'<a href="|</a>', "", i)

    i = re.split(r'">', i)
    urlss[i[0]] = i[1]

print(urlss)
for u in urlss.keys():
    print(urlss[u])
    test = gettag(u,r'div',"TRS_Editor")
   # test = getallpage(u,pattern=r'<div class="TRS_Editor"[\S|\s]+?</p> </div>')
    print(test)
"""
<div class="TRS_Editor"><p align="justify">　　<strong>一、A型题：1~90小题，每小题1.5分；91~120小题，每小题2分；共195分。在每一题给出的A，B，C，D四个选项中，请选出一项最符合题目要求的。</strong></p>
<p align="justify">　　1.下列关于机体内环境稳态的描述，错误的是</p>
<p align="justify">　　A.稳态是一种动态平衡</p>
<p align="justify">　　B.稳态的维持是机体自我调节的结果</p>
<p align="justify">　　C.稳态调节中都有一个调节点</p>
<p align="justify">　　D.稳态是指细胞内液理化性质基本恒定</p>
<p align="justify">　　2.在引起和维持细胞内外Na+、K+不对等分布中起重要作用的膜蛋白是</p>
<p align="justify">　　A.载体B.离子泵c.膜受体D.通道</p>
<p align="justify">　　3.神经细胞的静息电位为-70mV，Na+平衡电位为+60mV，Na+的电化学驱动力则为</p>
<p align="justify">　　A. -130mV B. -10mV C. +10mV D. +130mV</p>
<p align="justify">　　4.风湿热时，红细胞沉降率加快的原因是</p>
<p align="justify">　　A.红细胞表面积体积比增大B.血浆白蛋白、卵磷脂含量增高</p>
<p align="justify">　　C.血浆纤维蛋白原、球蛋白含量增高D.红细胞本身发生病变</p>
<p align="justify">　　5.阿司匹林通过减少TXA2合成而抗血小板聚集的作用环节是</p>
<p align="justify">　　A.抑制COX B.抑制TXA-,合成醇</p>
<p align="justify">　　C.抑制PGI7合成醇D.抑制PLA2;</p>
<p align="justify">　　6.心室肌细胞在相对不应期和超常期内产生动作电位的特点是</p>
<p align="justify">　　A.0期去极化速度快B.动作电位时程短</p>
<p align="justify">　　C.兴奋传导速度快D.0期去极化幅度大</p>
<p align="justify">　　7.在微循环中，进行物质交换的血液不流经的血管是</p>
<p align="justify">　　A.后微动脉B.通血毛细血管C.微静脉D.微动脉</p>
<p align="justify">　　8.下列呼吸系统疾病中，主要表现为呼气困难的是</p>
<p align="justify">　　A.肺气肿B.肺水肿C.肺纤维化D.肺炎</p>
<p align="justify">　　9.下列关于CO影响血氧运输的叙述，错误的是</p>
<p align="justify">　　A.CO中毒时血O2分压下降</p>
<p align="justify">　　B.CO妨碍O2与Hb的结合</p>
<p align="justify">　　C.C0妨碍O2与Hb的解离</p>
<p align="justify">　　D.CO中毒时血O2含量下降</p>
<p align="justify">　　10.下列关于颈动脉体化学感受器的描述，错误的是</p>
<p align="justify">　　A.其流入流出血液中的Pa02差接近零，通常处于动脉血环境中</p>
<p align="justify">　　B.Pa02降低、PaC02和H+浓度升高对其刺激有协同作用</p>
<p align="justify">　　C.感受器细胞上存在对02，C02、H+敏感的不同受体</p>
<p align="justify">　　D.血供非常丰富，单位时间内血流量为全身之冠
 </p> </div>
"""