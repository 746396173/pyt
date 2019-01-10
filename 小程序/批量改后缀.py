# coding=utf-8
import os
dir_path = r"F:\DIYpre\2018年12月6日140931"
new_extension = ".mp4"
os.chdir(dir_path)
for parent, dirnames, filenames in os.walk(dir_path,  followlinks=True):
        for filename in filenames:
            portion = os.path.splitext(filename)#分离文件名与后缀
            newname = portion[0]+new_extension
            os.rename(filename,newname)
            print(filename+"已更名为-->"+newname)




            #file_path = os.path.join(parent, filename)
            #print('文件名：%s' % filename)
            #print('文件完整路径：%s\n' % file_path)