class Cat(object):#定义类
	"""猫类"""
	#属性

	#方法

	def __init__(self,new_name,new_age):#init方法初始化对象	创建对象后会自动调用init方法
		self.name = new_name#初始化对象的属性
		self.age = new_age
		print("init方法")

	def __str__(self):#打印方法 没有此方法时,打印对象返回的事对象地址
		return "%s的年龄是:%d"%(self.name,self.age)




	def eat(self):#第一个形参self代表的是对象.一定要有,名字没要求 
		print("猫在吃")


	def drink(self):
		print("猫在喝")


	def introduce(self):
		print("%s的年龄是:%d"%(self.name,self.age))
#创建一个对象
Tom = Cat("汤姆",50)
print(Tom)

lanmao = Cat("蓝猫",10) #创建第二个对象

lanmao.introduce()




























