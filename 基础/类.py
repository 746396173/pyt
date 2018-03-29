# 类定义
class people:
	# 定义基本属性  构造中传入的属性不定义也可以
	banji="三年二班"
	name = ''
	age = 0
	# 定义私有属性,私有属性在类外部无法直接进行访问
	__weight = 0

	# 定义构造方法 传参数
	def __init__(self, n, a, w):
		self.name = n
		self.age = a
		self.__weight = w
		self.banji="三年三班"

	def speak(self):
		print("%s 说: 我 %d岁。%dkg" % (self.name, self.age, self.__weight))


# 实例化类
p = people('runoob', 10, 30)
p.speak()
print(p.age)
# print(p.__weight)   私有属性在类外部无法直接进行访问 包括子类

class student(people):
	chinese = 0
	english = 0
	pe		= 0
	math	= 0
	def __init__(self,n,a,w,c,e,p,m):
		people.__init__(self, n, a, w)##调用父类的构函
		self.chinese=c
		self.english=e
		self.pe		=p
		self.math	=m

	def pr(self):
		print("%s 说: 我 %d岁 成绩: 语文%d 英语%d 体育%d 数学%d"%(self.name, self.age, self.chinese, self.english, self.pe, self.math))


x = student("李明",19,60,60,60,60,60)
x.pr()

'''方法重写
如果你的父类方法的功能不能满足你的需求，你可以在子类重写你父类的方法，实例如下：

实例(Python
3.0 +)

# !/usr/bin/python3
'''
class Parent:  # 定义父类
	def myMethod(self):
		print('调用父类方法')


class Child(Parent):  # 定义子类
	def myMethod(self):
		print('调用子类方法')


c = Child()  # 子类实例
c.myMethod()  # 子类调用重写方法
super(Child, c).myMethod()  # 用子类对象调用父类已被覆盖的方法
'''super()
函数是用于调用父类(超类)
的一个方法。

执行以上程序输出结果为：

调用子类方法
调用父类方法
'''
