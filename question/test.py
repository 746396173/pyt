def A(func):
	print("A")
	return func
def B():
	print("B")
	#return "b返回值"

a=A(B())
print(a)