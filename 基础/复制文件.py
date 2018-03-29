import os


def fuzhi():#定义复制方法
	#1.获取要复制的文件名
	old_file_name = input("输入要复制的文件名:")
	path_houzhui = os.path.splitext(old_file_name)[1]# 获取要复制文件的后缀名
	path_mingcheng = os.path.split(old_file_name)[1]#获取文件名
	#print(path)
	#2.r只能开要复制的文件读取数据 文本读取文本文件，并且是UTF-8编码的文本文件。要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可
	with open(old_file_name, "rb") as f:
		content = f.read()
		#with语句不需要f.close()
	#3.新建一个文件
	new_file = open(path_mingcheng+"[副本]"+path_houzhui,"wb")#复制到目录


	#4.写入新文件中
	new_file.write(content)
	new_file.close()

fuzhi()