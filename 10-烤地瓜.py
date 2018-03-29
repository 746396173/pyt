class SweetPotato(object):#定义地瓜类

	def __init__(self):
		self.cookedString = "生的"#地瓜状态
		self.cook_time = 0#烤的时间
		self.peiliao=[]#加的配料
	def cook(self,time):#烤方法
		self.cook_time += time 
		if self.cook_time <= 3:
			self.cookedString  = "生的"
		elif self.cook_time <= 5:
			self.cookedString = "半生不熟"
		elif self.cook_time <= 8:
			self.cookedString = "烤好了"
		else:
			self.cookedString = "已经成木炭了"
	def addliao(self,liao):#加料方法
		self.peiliao.append(liao)

	def __str__(self):#返回信息
		liao_msg=""
		msg = "已经烤了%d分钟,现在是%s"%(self.cook_time,self.cookedString)
		if len(self.peiliao)>0:#判断是否加了配料
			for liao in self.peiliao:
				liao_msg +=liao+" " 
			liao_msg ="配料用了%s"%(liao_msg) 
			msg = msg+liao_msg
		return msg
		

#创建地瓜对象
d = SweetPotato()
d.cook(1)
d.cook(5)
d.addliao("番茄酱")
d.addliao("孜然")
print(d)		