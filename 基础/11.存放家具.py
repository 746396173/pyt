class HOME:
	def __init__(self,new_area,new_info,new_adder):
		self.area = new_area
		self.info = new_info
		self.adder = new_adder
		self.left_area=new_area
		self.contain_items = []
	def __str__(self):
		msg =  "房子面积是:%d,可用面积是:%d,户型是:%s,地址是:%s,"%(self.area ,self.left_area,self.info,self.adder)
		msg += "房子里有%s"%(str(self.contain_items))
		return msg

	def add_item(self,item ):#通过方法获取另类对象的属性,可以控制属性的获取权限.而不应该直接获取	
		self.left_area = self.area-item.get_area()
		if self.left_area > 0:
			self.contain_items.append(item.get_name())
		else:
			self.left_area += item.get_area()
			print( "空间不足,无法放置")
class Bed:
	def __init__(self,new_name,new_area):
		self.name = new_name
		self.area = new_area
	def __str__(self):
		return "%s占用的面积是%d"%(self.name,self.area)
	def get_area(self):
		return self.area
	def get_name(self):
		return self.name 


fangzi = HOME(126,"三室一厅","北京市")
print(fangzi)
bed1 = Bed("席梦思",4)
bed2 = Bed("三人床",600)
print(bed1)
fangzi.add_item(bed1) #引用对象bed1
fangzi.add_item(bed2)
print(fangzi)
