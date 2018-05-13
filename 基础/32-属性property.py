class Student(object):
	def __init__(self):
		self.__name = ""

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self,name):
		if 2<=len(name) <=6:
			self.__name = name
		else:
			print("输入有误?")

xiao = Student()
xiao.name = "小明"
print(xiao.name)