from bs4 import BeautifulSoup
import re
import os
import requests
import json
import time
import lxml
import OpenSSL
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

mainsite = "http://t66y.com/"
def getbs(url):#获取页面源代码
    firefox_options=Options()
    firefox_options.add_argument("-headless")
    browser = webdriver.Firefox(firefox_options=firefox_options)
    #browser = webdriver.PhantomJS()
    #路径在D:\app\ANACONDA\phantomjs
    browser.set_window_size(1000, 500)  # 分辨率 1024*768
    # 设定页面加载timeout时长，需要的元素能加载出来就行
    browser.set_page_load_timeout(200)
    browser.set_script_timeout(200)
    try:
        browser.get(url)
    except:
        print("加载页面太慢，停止加载，继续下一步操作")
        browser.execute_script("window.stop()")
    #print(browser.page_source)
    req=browser.page_source
    browser.close()
    bsobj = BeautifulSoup(req, "lxml")
    return bsobj

def getallpageArticleurl(start,end):#取得所设页面的所有文章链接与标题
    urls=[]
    for i in range(start,end+1):
        url = "http://t66y.com/thread0806.php?fid=16&search=&page={}".format(str(i))
        bsobj = getbs(url)
        #print(bsobj)
        urls += bsobj.find_all("a", href = re.compile("^htm_data.*"),id=True)
    print(urls)
    urltitle = [(mainsite + i['href'],i.text) for i in urls]
    titlenumber = len(urltitle)
    print('文章总数目'+str(titlenumber))
    return urltitle#[(url,title),(),(),()]

def getpicofpage(url):
    pattern = r'src="http[\S]+?"'
    paths = "F:/photos/se/2018-12-4/"
    bsobj=getbs(url)
    div=bsobj.find("div",{"class":"tpc_content do_not_catch"})
    if div==None:

        print("获取不到内容，跳过")
        return -1
    inputs=div.find_all("input")
    print(inputs)
    title=bsobj.find("h4").text
    title = re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+", "",title)########研究一下
    if inputs==[]:
        print("本页无图片，跳过")
        return -1
    num=1
    if os.path.exists(paths + title)==False:

        os.makedirs(paths  + title)#mkdir只能创建一层新目录,makedirs多层
    else:
        print("已存在该文件夹，跳过")
        return -1
    for i in inputs:
        try:#问题主要出在这里
            i=str(i)
            #print("此图片地址块是"+i)
            result = re.findall(pattern, i)[0]
            result=str(result[5:-1])
            print('提取到的地址是'+result)

            res = requests.get(result,timeout=150)
            with open(paths +title+"/"+str(time.time())[:10]+".jpg", 'wb') as f:
                f.write(res.content)
        except  BaseException as e:
                print(e)
                continue


def docaiji(urlstitle):
    page = 1
    ed = []
    for i in urlstitle:
        if i in ed:
            print(i[1] + "本篇已采集过，跳过,剩余"+len(urlstitle)-page)
            continue
        getpicofpage(i[0])
        ed.append(i)
        print("采集完第{}篇{},剩余{}篇".format(page,i[1],len(urlstitle)-page ))
        page += 1
        time.sleep(1)


urls = getallpageArticleurl(2,10)
print(urls)
docaiji(urls)
