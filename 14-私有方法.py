class Dog(object):
	"""docstring for Dog"""
	def __test1(self):#__方法定义私有方法
		print("........正在发送短信.........")

	def send_msg(self,new_money):#此方法验证是否有资格调用__test1
		if  new_money>10000:
			self.__test1()
		else:
			print("请充值")
	def __init__(self):
		pass		
dog = Dog()
dog.send_msg(100)
dog.__test1()#私有方法不能直接调用