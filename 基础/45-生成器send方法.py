def test():
    i = 0
    while i<5:
        temp = yield i#第一次取值后停在这里,将 (yield 返回值 )  保存到temp 默认值为None 但此时可通过send(值)可给yield i 整体赋值
        print(temp)#输出temp的赋值
        i +=1

t =test()
t.send(None)#在迭代器还没有开启时,若要用send(),只能穿None
print(t.__next__())
print(t.__next__())
t.send("强势插入")#给temp赋值,不能第一次迭代就给send()赋值为非None
print(next(t))
"""send()作用: 可给特定的生成器值传参数"""
