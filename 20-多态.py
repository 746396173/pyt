class F1(object):
	"""docstring for F"""
	def show(self):
		print("F1.show")
		
class F2(F1):
	def show(self):
		print("F2.show")

def Func(obj): #多态,指对一个函数来说,传入不同的对象有不同的执行.
	obj.show()

f1 = F1()
f2 = F2()
Func(f1)
Func(f2)
