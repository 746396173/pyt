class A(object):
	"""docstrin A"""
	def __init__(self):
		self.numl = 100
		self.__num2 = 200

	def test1(self):
		print(".....test1......")		
		self.__test2()

	def __test2(self):
		print("......test2......")

class B(A):
	def test3(self):
		super.test1()
		# super.__test2() #不能调用父类的私有属性与方法

b = B()
b.test1()
b.test3()

