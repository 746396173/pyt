def w1(func):#闭包函数
    print("w1正在装饰")
    def inner():
        print("验证1")
        # 验证1
        # 验证2
        # 验证3
        func()#调用内部函数
    return inner

def w2(func):
	print("w2正在装饰")
	def inner():
		print("验证2")
		func()
	return inner
@w1 #解释器到这里就会执行w1函数 ，并将 @w1 下面的函数作为w1函数的参数，即：@w1 等价于 w1(f1) 所以，内部就会去执行
@w2
def f1():
	print('f1')

f1()