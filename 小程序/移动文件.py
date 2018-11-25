# coding=utf-8
import os
import shutil
dir = os.getcwd()
files = os.listdir(dir)
print(files)
files.remove("移动文件.py")
print(files)

for file in files:
    olddir = os.path.join(dir,file)
    newdir = os.path.join(r"F:\记录片\bbc蓝色星球",file)
    shutil.move(olddir,newdir)  # 移动文件或目录
