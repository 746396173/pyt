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
		try:
			ext = os.path.splitext(each_file)[1]  # os.path.splitext(path) 分离文件名与扩展名；默认返回(fname,fextension)元组，可做分片操作\
			if ext in target:
				vedio_list.append(os.getcwd() + os.sep + each_file + os.linesep)
			if os.path.isdir(each_file):
				search_file(each_file, target)  # 递归调用
				os.chdir(os.pardir)  # 递归调用后切记返回上一层目录
		except:
			continue#continue要放在for语句内

start_dir = input('请输入待查找的初始目录：')
if os.path.exists(start_dir):
	program_dir = os.getcwd()

	target = ['.mp4', '.avi', '.rmvb','.jpg']
	vedio_list = []
	search_file(start_dir, target)
	f = open(program_dir + os.sep + 'vedioList.txt', 'w')
	f.writelines(vedio_list)
	f.close()
else:
	print("文件夹不存在")