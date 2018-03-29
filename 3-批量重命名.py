import os
def gaiming():
	"批量重命名"
	file_name = input("需要重命名的完整文件目录(末尾加分隔符):")
	dir_list = os.listdir(file_name)
	n = 1
	for name in dir_list:
		file_houzhui = os.path.splitext(name)[1]
		new_name = "0"*(7-len(str(n)))+str(n)+file_houzhui
		os.rename(file_name+name,file_name+new_name)
		n+=1

	new_dir_list = os.listdir(file_name)
	print(new_dir_list)
gaiming()