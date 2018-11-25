# coding=utf-8
from unrar import rarfile
import os
dir = os.getcwd()
filerar = os.path.join(dir, "glasswire.elite.pjb.rar")
dirname =os.path.splitext(filerar)[0]
os.mkdir(dirname)#新建不带扩展名的同名目录

file = rarfile.RarFile(filerar)  #这里写入的是需要解压的文件，别忘了加路径
file.extractall(dirname)  #这里写入的是你想要解压到的文件夹

