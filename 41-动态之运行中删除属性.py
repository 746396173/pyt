import time
class students():

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return "name=%s,age=%d"%(self.name,self.age)

a = students("xiaoming",10)
print(a.age)
print(a.name)
a.cla = "三年级"#运行中添加属性
print(a.cla)
time.sleep(2)
del a.cla#删除属性  cla
print(a.cla)
