from bs4 import BeautifulSoup

import re
import os
import requests
import json
import time
import lxml
import OpenSSL
mainsite="http://t66y.com/"
def getbs(url):
        header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
                "Referer":"http://t66y.com//thread0806.php?fid=16&search=&page=1",
                "Host":"t66y.com"
                }
        req=requests.get(url,headers=header)
        req.encoding="gbk"#这里因为1024图片帖子内的编码是gbk,如果不指明编码，得到的是乱码
        bsobj = BeautifulSoup(req.text, "lxml")
        return bsobj

def getallpage(start,end):
        urls=[]
        for i in range(start,end+1):
                url="http://t66y.com/thread0806.php?fid=16&search=&page={}".format(str(i))
                bsobj=getbs(url)
                urls+=bsobj.find_all("a",{"href":re.compile("^htm_data.*")})
        return urls
def getpicofpage(url):
        pattern = r'src="http[\S]+?"'

        paths = "F:/photos/se/"
        bsobj=getbs(url)
        div=bsobj.find("div",{"class":"tpc_content do_not_catch"})
        if div==None:
                print("获取不到内容，跳过")
                return -1
        inputs=div.find_all("input")
        print(inputs)
        title=bsobj.find("h4").text
        if inputs==[]:
                print("本页无图片，跳过")
                return -1
        num=1
        if os.path.exists(paths + title)==False:
                os.mkdir(paths  + title)
        else:
                print("已存在该文件夹，跳过")
                return -1
        for i in inputs:
                try:#问题主要出在这里
                    i=str(i)
                    print("i的值是"+i)
                    result = re.findall(pattern, i)[0]
                    result=str(result[5:-1])
                    print(result)

                    res = requests.get(result,timeout=25)
                    with open(paths +title+"/"+str(time.time())[:10]+".jpg", 'wb') as f:
                        f.write(res.content)
                except  BaseException as e:
                        print(e)
                        return -1

l=getallpage(1,10)
page=1
ed=[]
for i in l:
        url=mainsite+i["href"]
        if url in ed:
                print(url+"本页已采集过，跳过")
                continue
        print(url)
        getpicofpage(url)
        ed.append(url)
        print("采集完第{}页".format(page))
        page+=1
        time.sleep(3)