class Tool(object):
	"""docstring for Tool"""
	#类属性
	num = 0
	#类方法
	def __init__(self,name):
		self.name = name
		Tool.num += 1


tool = Tool("锤子")
tool2 = Tool("刀子")
print(tool.num)
print(Tool.num)


