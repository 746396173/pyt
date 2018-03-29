'''a,b=0,1
while b<10:
	print(b)
	a,b=b,a+b

age=int(input("请输入你家狗的年龄:"))
print("")
if age<0:
	print("你在逗我?")
elif age==1:
	print("相当于14岁的人.")
elif age==2:
	print("相当于22岁的人")
elif age>2:
	human=22+(age-2)*5

	print("相当于",human,"岁的人")
input("点击enter键退出")
'''
####while循环
n=100
sum=0
i=1
while i<=100:
	sum=i+sum
	i=i+1
else:
	pass
print ("1到%d之和为:%d" %(n,sum))

languages=["c","c++","python"]
for x in languages:
	print(x)
	if x=="python":
		print("找到了")
		break
	print("循环数据"+x)
else:#循环数据源为空时执行
	print("没有循环数据!")
print("完成循环!")

"""range()函数,生成数列  range(列出x个数), range(起始值,终止值序号) range(起始值,终止值序号,指定步数)"""
for i in range(3):
	print(i)

for i in range(3,5):
	print(i)

for i in range(0,5,1):
	print(i)

#遍历序列
a=["google","baidu","runoob"]
for i in range(len(a)):
	print(i,a[i])

for i,j in enumerate(a):#使用函数遍历序列
	print(i,j)

#range()创建一个列表
a=list(range(5,100,3))
print(a)

#for循环字符串时,字符一个个被取出
for letter in "人生苦短,我选python":
	if letter=="n":
		break #退出循环体
	print("当前字母为:",letter)
print("goodbye")

#pass语句不起任何作用
