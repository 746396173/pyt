class students():
    __slots__ = ("name","age")#对象只能用__slots__里的属性
    def __init__(self,name,age=9):
        self.name = name
        self.age = age

    def __str__(self):
        return "name=%s,age=%d"%(self.name,self.age)

a = students("xiaoming")
print(a.age)
print(a.name)
