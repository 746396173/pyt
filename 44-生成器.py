"""在python中,一边循环一边计算的机制,称为生成器,与列表生成式相比
可节省大量的内存空间并能记住当前所在位置"""
#创建生成器的方法:
#1.将列表生成式的[]改为()
import time
l=[x*2 for x in range(6)]
print(l)
g = (x*2 for x in range(6))
print(next(g))
print(next(g))
for g in g:
    print(g)
print("------g循环结束--------")
#2.通过带有yield 返回值 的函数创建
def fin (times):
    n = 0
    a,b =0,1
    while n<times:
        yield b
        a,b = b, a + b
        n+=1
    return "done"

print (next(fin(10)))
for fi in fin(10):
    print(fi)
    #break
time.sleep(1)
print("----等待结束-------")
ff = fin(5)
while True:
    print(next(ff)) #使用next()遍历生成器后会抛出StopIteration异常