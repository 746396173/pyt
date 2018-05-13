class Cat(object):#定义类
	"""猫类"""
	#属性

	#方法
	def eat(self):
		print("猫在吃")


	def drink(self):
		print("猫在喝")


	def introduce(self):
		print("%s的年龄是:%d"%(Tom.name,Tom.age))
#创建一个对象
Tom = Cat()

Tom.eat()#调用指向对象的方法

Tom.name = "汤姆"#词句相当于添加了一个属性
Tom.age = 60

print("%s的年龄是:%d"%(Tom.name,Tom.age))#获取属性第一种方法
Tom.introduce()#第二种方法