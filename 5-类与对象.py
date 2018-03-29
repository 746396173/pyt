class Cat(object):#定义类
	"""猫类"""
	#属性

	#方法
	def eat(self):
		print("猫在吃")


	def drink(self):
		print("猫在喝")


#创建一个对象
Tom = Cat()
Tom.eat()
Tom.name = "汤姆"#词句相当于添加了一个属性
print(Tom.name)


