import os
import re
import datetime    #调用事件模块
today = datetime.date.today()
ISOFORMAT='%Y-%m-%d' #设置输出格式
today = today.strftime(ISOFORMAT)
def gaiming():
    global today
    "批量重命名"
    file_name = input("需要重命名的完整文件目录(末尾加分隔符):")
    cishu = input("输入今日第几次修改，回车默认为1：")#程序今日运行次数，防止重名
    if cishu =="":
        cishu = 1

    dir_list = os.listdir(file_name)
    pattern = r"^YR-|^\."
    n = 1
    for name in dir_list:
        if re.match(pattern,os.path.splitext(name)[0]) == None :

            file_houzhui = os.path.splitext(name)[1]#结果为 .jpg形式
            new_name = "YR-"+today+str(cishu)+"0"*(3-len(str(n)))+str(n)+".jpg"
            os.rename(file_name+name,file_name+new_name)
            n+=1

    new_dir_list = os.listdir(file_name)
    print(new_dir_list)
gaiming()