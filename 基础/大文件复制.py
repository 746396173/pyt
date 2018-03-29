"""read()读所有内容
	readline()读一行
	readlines()readlines可以按照行的方式把整个文件中的内容进行一次性读取，并且返回的是一个列表，其中每一行的数据为一个元素
大文件大于内存时.直接读会无法读取
"""

import os
def fuzhi():
	#1.获取要复制的文件名
	old_file_name = input("输入要复制的文件名:")
	path_houzhui = os.path.splitext(old_file_name)[1]# 获取要复制文件的后缀名
	path_mingcheng = os.path.split(old_file_name)[1]#获取文件名
	#print(path)
	#2.新建一个文件
	new_file = open(path_mingcheng+"[副本]"+path_houzhui,"ab")#复制到当前目录
	#3.r只能开要复制的文件读取数据 文本读取文本文件，并且是UTF-8编码的文本文件。要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可
	with open(old_file_name, "rb") as f:
		while True:
			content = f.read(1024)  # 一次读取1024个字节,避免内存问题
			if len(content)==0:
				break
			new_file.write(content)#写入
		#with语句不需要f.close()
	new_file.close()

fuzhi()