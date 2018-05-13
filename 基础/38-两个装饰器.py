def w1(func):#闭包函数
    print("w1正在装饰")
    def inner():
        print("验证1")
        func()#调用内部函数
    return inner

def w2(func):
    print("w2正在装饰")
    def inner():
        print("验证2")
        func()
    return inner
@w1
@w2
#解释器走到这里,会先执行w2等价于w2(f1),在执行w1 等价于w1(w2(f1)),
# 当调用f1()时执行为==>w1闭包内函数调用w2闭包内函数(f1),
# 然后w2内函数调用f1()执行'''
def f1():
    print('f1')

f1()