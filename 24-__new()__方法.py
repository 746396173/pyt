class A(object):
	def __init__(self):#实例方法>>>>self 就是创造出的实例对象
		print("init方法传入的self:%d"%(id(self)))
		print("这是init方法")

	def __new__(cls):
		print("A类__new__方法cls:%d"%(id(cls)))
		print("这是new方法")
		ret = object.__new__(cls)
		print("objtct.__new__(cls)创造出的实例对象地址:%d"%(id(ret)))
		return ret


print(id(A))
a = A()
#b = A()
print(id(a))

'''A类通过调用父类的__new__(cls)方法创建出一个实例对象,实例方法__init__(self)对传入的实例对象self初始化'''
"""结果:
id(A):37572072
A类__new__方法cls:37572072	__new__()方法
这是new方法
objtct.__new__(cls)创造出的实例对象地址:139652785060552
init方法传入的self:139652785060552		
这是init方法
实例a的地址: 139652785060552
"""