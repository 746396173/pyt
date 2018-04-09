import  re
t =""
with open("t.txt","r+",encoding='UTF-8')as txt:
    t = txt.read()
print(t)#原始文本
pattern = r"<[\S]{1,4}>|&nbsp;"
result = re.sub(pattern, "",t)#替换匹配值
print(result)


"""提取图片地址"""
t =r'<img data-original="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg"" style="display: inline;">'
pattern =r'src="[\S]+?"'
result =re.findall(pattern,t)
print(result)
