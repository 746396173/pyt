# coding=utf-8
from unrar import rarfile
import os
dir = os.getcwd()
filerar = os.path.join(dir, "glasswire.elite.pjb.rar")
dirname =os.path.splitext(filerar)[0]
os.mkdir(dirname)#新建不带扩展名的同名目录

file = rarfile.RarFile(filerar)  #这里写入的是需要解压的文件，别忘了加路径
file.extractall(dirname)  #这里写入的是你想要解压到的文件夹

'''
#os.path的几种用法

#filename为绝对路径（例如：D:\Example\Demo.zip）

os.path.split(filename)[0]      #文件所在的文件夹路径     即:D:\Example\

os.path.splitext(filename)[0]  #无扩展名的绝对路径       即:D:\Example\Demo

os.path.splitext(filename)[1]   #文件扩展名                    即: zip

os.path.basename(os.path.splitext(filename)[0]) #文件名   即：Demo


'''