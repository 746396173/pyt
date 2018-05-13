def func (functionName):
    def func_in(*args,**kwargs):#对有无参数的函数通用
        print("----记录日志-------")
        return functionName(*args,**kwargs)#对有无返回值函数通用
    return func_in

@func
def test():
    print("---test-----")
    return "haha"

@func
def test2():
    print("-----test2--------")

@func
def test3(a):
    print("--------test3---a=%d--"%a)
@func
def test4(a,b):
    print("--------test4--a=%d,b=%d--------"%(a,b))

test()
test3(3)