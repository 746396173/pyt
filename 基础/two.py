

print(list(range(5)))
'''Python3 range() 函数返回的是一个可迭代对象（类型是对象），而不是列表类型， 所以打印的时候不会打印列表。

Python3 list() 函数是对象迭代器，可以把range()返回的可迭代对象转为一个列表，返回的变量类型为列表。

Python2 range() 函数返回的是列表。'''
import sys

print('命令行参数如下:')
for i in sys.argv:
   print(i)

print('\n\nPython 路径为：', sys.path, '\n')

import fibo#引入模块
fibo.fib(1000)
print(fibo.fib2(1000))
"""如果你打算经常使用一个函数，你可以把它赋给一个本地的名称："""
fib = fibo.fib
fib(500)
"""from…import 语句
Python的from语句让你从模块中导入一个指定的部分到当前命名空间中，语法如下：

from modname import name1[, name2[, ... nameN]]"""
from fibo import fib
fib(100)

str1 = "菜鸟教程";
str_utf8 = str1.encode("UTF-8")
str_gbk = str1.encode("GBK")

print(str1)

print("UTF-8 编码：", str_utf8)
print("GBK 编码：", str_gbk)

print("UTF-8 解码：", str_utf8.decode('UTF-8','strict'))
print("GBK 解码：", str_gbk.decode('GBK','strict'))

# from urllib import request
#
# response = request.urlopen("http://www.baidu.com/")  # 打开网站
# fi = open("project.txt", 'w')
# # open一个txt文件
# page = fi.write(str(response.read()))                # 网站代码写入
# fi.close()

"""str.format() 的基本使用如下:"""
"""括号及其里面的字符 (称作格式化字段) 将会被 format() 中的参数替换。
在括号中的数字用于指向传入对象在 format() 中的位置，如下所示："""
"""如果在 format() 中使用了关键字参数, 那么它们的值会指向使用该名字的参数。"""
print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))
print('{0} 和 {1}'.format('Google', 'Runoob'))
print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))

table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}#字典键与值
print(table['Taobao'])

print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))

import os

'''递归查找视频文件'''
'''python中os.path常用模块
os.path.sep:路径分隔符      linux下就用这个了’/’
os.path.altsep: 根目录
os.path.curdir:当前目录
os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。这个列表以字母顺序。 它不包括 '.' 和'..' 即使它在文件夹中。
os.path.pardir：父目录
os.path.abspath(path)：绝对路径
os.path.join():       常用来链接路径
os.path.split(path):      把path分为目录和文件两个部分，以列表返回
'''
def search_file(start_dir, target):
   os.chdir(start_dir)# os.chdir() 方法用于改变当前工作目录到指定的路径。

   for each_file in os.listdir(os.curdir):
      ext = os.path.splitext(each_file)[1]#os.path.splitext(path) 分离文件名与扩展名；默认返回(fname,fextension)元组，可做分片操作
      if ext in target:
         vedio_list.append(os.getcwd() + os.sep + each_file + os.linesep)
      if os.path.isdir(each_file):
         search_file(each_file, target)  # 递归调用
         os.chdir(os.pardir)  # 递归调用后切记返回上一层目录


start_dir = input('请输入待查找的初始目录：')
program_dir = os.getcwd()

target = ['.mp4', '.avi', '.rmvb']
vedio_list = []

search_file(start_dir, target)

f = open(program_dir + os.sep + 'vedioList.txt', 'w')#os.sep文件夹分隔符
f.writelines(vedio_list)
f.close()


