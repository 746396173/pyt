class Dog(object): 
	"""设置属性应该通过方法去设置,这样可以对输入的值进行判断,从而避免非法"""
	def __init__(self):
		pass

	def set_age(self,new_age):
		if new_age >0 and new_age <=100:
			self .gae = new_age
		else:
			self.age = 0

		
dog = Dog()
dog .age = -10
print(dog.age)	
dog.set_age(5)
print(dog.age)
dog.set_age(120)
print(dog.age)