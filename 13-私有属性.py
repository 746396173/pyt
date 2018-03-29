class Dog(object): 
	"""设置属性应该通过方法去设置,这样可以对输入的值进行判断,从而避免非法"""
	def __init__(self):
		self.__age = 0 #初始化私有属性
	def set_age(self,new_age):#设置私有属性
		if new_age >0 and new_age <=100:
			self .__age = new_age
		else:
			self.__age = 0
	def get_age(self):#取出私有属性
		return self.__age 
		
dog = Dog()
print(dog.get_age())
dog.set_age(5)
print(dog.get_age())
dog.set_age(120)
print(dog.get_age())