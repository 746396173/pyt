l = list(range(10,78))#
print(l)
l = list(range(10,78,2))#range(起始,终止,步长)返回的时一个列表的对象
print(l)
a = [i*i  for i in range(180)]
print(a)
a = [i for i in range(100) if i % 2==0]
print(a)
a = [1 for i in range(2) for j in range(2)]
print(a)#结果为 1 1 1 1
a = [(i,j) for i in range(2) for j in range(2)]
print(a)#[(0, 0), (0, 1), (1, 0), (1, 1)]