class TestLongError (Exception):#自定义异常类
	def __init__(self,test_l,will_l):
		super.__init__()
		self.test_l = test_l
		self.will_l = will_l


def intest ():
	try:
		L = input("输入")
		test_l = len(L)
		if test_l < 3:
			raise TestLongError(test_l,3)
	except TestLongError as result :		
			print("TestLongError:"+str(result))
	else:
			print("无异常")

intest()