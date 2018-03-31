import	types
import time
class students():
    num = 1000
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return "name=%s,age=%d"%(self.name,self.age)

#定义⼀个实例⽅法
def	run(self,speed):
    print("%s在移动,	速度是%d km/h"%(self.name,speed))
#定义⼀个类⽅法
@classmethod
def	testClass(cls):
    cls.num	=	100
#定义⼀个静态⽅法
@staticmethod
def	testStatic():
    print("---static	method----")

A = students("a",10)
#为对象添加实例方法
A.run = types.MethodType(run,A)#赋值号左边的函数名可和绑定的不一致
A.run(100)
#给Person类绑定类⽅法
students.testClass = testClass
#调⽤类⽅法
print(students.num)
students.testClass()
print(students.num)
#给Person类绑定静态⽅法
students.testStatic	=	testStatic
students.testStatic()
