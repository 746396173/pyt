def w1(func):#闭包函数
    print("正在装饰")
    def inner(*args):
        print("验证")
        # 验证1
        # 验证2
        # 验证3
        func(*args)#调用被修饰函数
    return inner#不写括号表示返回函数引用,如果加()表示调用,实际上此出返回的是   被外层函数修饰过得f1函数的引用inner = f1=w1(f1)

@w1 #解释器到这里就会执行w1函数 ，并将 @w1下面的函数作为w1函数的参数，即：@w1+def被修饰函数 等价于 f1=w1(f1)
def f1():
    print('f1')
@w1
def f2():
    print('f2')
@w1
def f3(a):#有参数的函数的修饰,因为inner就是被修饰的f3,所以inner()中应该有f3的参数
    print('f3---%d'%a)
@w1
def f4():
    print('f4')

f3(3)