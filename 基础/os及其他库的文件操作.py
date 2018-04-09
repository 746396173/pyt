import shutil
import os
print(os.name )#posix为linux nt 为Windows系统
ab = os.path.abspath(".")#查看当前目录绝对路径
print(ab)
jo = os.path.join("path" ,"paths")#依据系统将两个目录路径连接起来
print(jo)
os.path.split("/user/michael/file.txt") #将目录分成两部分,后一部分总是最后级别的目录或文件
os.path.splitext("/user/fi.txt")#分割出文件扩展名


with open("test.txt","a+")as nf:#打开一个文件 如不存在则创建
    nf.write("a")
    nf.seek(0,0)#指针移动到文件首
    nfr = nf.read()
print(nfr)

'''
os.remove ("testrename.py")#删除文件

os.rename("test.txt","testrename.py")#文件重命名
'''

shutil.copyfile("test.txt","test[副本].txt")
with open("test[副本].txt","r+") as cf:
    cfr = cf.read()
print(cfr)

mulu = [x for x in os.listdir('C://') if os.path.isdir(os.path.join("C://" ,x))]#列出路径所有目录(非本目录,isdir()参数要求绝对路径)
print(mulu)
print(os.listdir("C://"))