""""给出两个相同长度的字符a和b构成的字符串,定义他们的距离为对应位置不同的自负的数量,如串"baa"和串"baa"的距离为0
串aab与串aba的距离为2,下面给出两个字符串S与T,其中S的长度不小于T的长度,我们用|s|代表S的长度,|T|代表
T的长度,那么在S中一共有|S|-|T|+1个与T长度相同的子串,现在你需要计算T串与这些子串的距离之和"""

S = input("输入字符串S")#长串
T = input("输入字符串T")#短串
"""

i = 0
while i < end_l:
	S_zi = S[i:i+T_len]
"""
S_len = len(S)
T_len = len(T)
i=0
end_l = S_len-T_len#最后一个子串的第一个元祖对象的位置
s_t = tuple(S)
t_t = tuple(T)
long = 0
while i <= end_l:
	s_t = s_t[i:]
	for item in zip(s_t,t_t): #zip 内置函数将俩个元祖相对应位置迭代输出,最短的元祖耗尽时停止
		if item[0] == item[1]:
			pass
		else:
			long +=1
	i +=1
else:
	print(long)