class Animal(object):#父类
	"""docstring for Animal"""
	def __init__(self,age):
		self.age = age

	def drink(self):
		print(".....喝.....")

	def eat(self):
		print(".....吃......")

class Dog(Animal):#继承-子类
	def __init__(self,name,age):#重写
		self.name = name 
		self.age = age
	
	def catch(self):
		print("....捉老鼠.....")

	def __str__(self):
		return "%s%d岁了"%(self.name,self.age)


class Xtq(Dog):#孙子类--子类可以继承父类的父类
	def fly(self):
		print("....飞......")

	def eat(self):#重写
		print(".....吃仙人掌........")

xiaotianquan = Xtq("哮天犬",500)
xiaotianquan.eat()
xiaotianquan.fly()
print(xiaotianquan)

bosi = Dog("波斯",5)
print(bosi)
bosi.eat()#直接使用父类方法
bosi.catch()
