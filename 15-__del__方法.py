import sys
class Dog(object):
	"""docstring for Dog"""
	def __init__(self):
		pass
	def __del__(self):#当对象的引用全都被删除后自动调用__del__方法
		print(".......对象被删除........")

dog1 = Dog()
dog3 = Dog()
del dog3
dog2 = dog1	#dog2指向同一个对象内存,并没有创造新对象 此对象引用计数为2
n = sys.getrefcount(dog2)#对象引用计数
print(n)
print(dog1,dog2)
del dog1 #del 删除的是引用 对象仍然存在
print(dog2)
#程序结束时,对象也会被删除
