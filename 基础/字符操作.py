T="what do you do"
# print(T[0:-1])#两个参数,上限下限(包括起始不包括终止)
# print(T[-1])#一个参数,索引引用
# print(T[6:])#默认到末尾
# print(T[:6])
# l=len(T)#字符串长度
# print(l)
# l=T[::-1]#第三个参数表步数 -1时倒序
# print(l)
#
# url="http://pythonadc.org"
# print(url[-3:])
# print(url[7:])#从索引7开始取值
# print(url[7:-4])
#ctrl+/注释选中部分

print(len(T))
for i in range(0,len(T)-1,2):#语法：range(stop) range(start, stop[, step]) 左闭右开
	print(T[i]+T[i+1],i)

sub="o"
print(T.count(sub,0,13))#count() 方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。

#字符加密解密
'''
m = input("输入要加密的信息:")
M=m.upper()
sub=""
#输入信息 并转变为大写字母(unicode编码为两位)
for i in M:
	sub=sub+str(ord(i))
print(sub)
#循环读取每个字符并加入密文中

#解密:
n=""
for i in range(0,len(sub)-1,2):
	m=chr(int(sub[i]+sub[i+1]))
	n=n+m
	n=n.lower()
	n=n.capitalize()
print(n,end="")


#将收到的密文分割
'''
#迭代器
def add(s, x):
 return s + x

def gen():
 for i in range(4):
  yield i

base = gen()
for n in [1, 10]:
 base = (add(i, n) for i in base)
print (list(base))

import sys


def fibonacci(n):  # 生成器函数 - 斐波那契
	a, b, counter = 0, 1, 0
	while True:
		if (counter > n):
			return
		yield a
		a, b = b, a + b
		counter += 1#counter每次加一


f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

while True:
	try:
		print(next(f), end=" ")
	except StopIteration:
		break
		#sys.exit()
print("")
#
# is 与 == 区别：
# is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等
# >>>a = [1, 2, 3]
# >>> b = a
# >>> b is a
# True
# >>> b == a
# True
# >>> b = a[:]
# >>> b is a
# False
# >>> b == a
# True


a=[1,2,3]
b=a #将a的内存地址赋予b
def to(a,b):#定义函数to()
 if b is not a:#is 用于判断两个变量引用对象是否为同一个
	 print("true")
 else:
	 print("flase")
to(a,b)
b=a[:] #将a的值赋予b
to(a,b)
"""定义一个函数
你可以定义一个由自己想要功能的函数，以下是简单的规则：
函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
函数内容以冒号起始，并且缩进。
return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
Python 定义函数使用 def 关键字，一般格式如下：
def 函数名（参数列表）:
    函数体
"""


def printinfo(name="", age=10):#默认参数要放后面,否则报错
	"打印任何传入的字符串"#函数说明
	print("名字: ", name);
	print("年龄: ", age);
	return;


# 调用printinfo函数
printinfo(age=50, name="runoob");
print("------------------------")
printinfo();

"""函数方法对于函数外不可变类型变量操作只能是在函数内更改其引用,对于可变类型操作可更改其引用,也可更改其属性从而更改其内存值
所以只有更改了外层变量的内存而非引用才能真正使其操作在外层起作用"""
a="hello"
def change(a):
	a="world"+a
	print(a)
	return

change(a)
print(a)

a=[1,2,3]
def change(a):
	a=[4,5,6]
	print(a)
	return
change(a)
print(a)

def change(a):
	#a = [0]
	a.append(4)
	print(a)
	return
change(a)
print(a)
'''函数内可通过global更新全局变量'''
a=10
def change(b):
	global a # 需要使用 global 关键字声明
	print(a)
	a=11
	return
change(a)
print(a)

