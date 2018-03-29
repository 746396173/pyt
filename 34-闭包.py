def name(name):#外函数
	def in_name(name_in):
		print("name=%s,in_name = %s"%(name,name_in) )
		return "%s%s"%(name,name_in)
	return	in_name#返回闭包函数

n = name("xiaoming")#n指向闭包函数
print(n("小明"))

"""构建闭包函数可以用来将外函数的变量传递给内涵数"""