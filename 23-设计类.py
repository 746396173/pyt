class Car(object):#车类
	def move(self):
		print("车在移动")
	def music(self):
		print("正在放音乐")
class Suonata(Car):
	def info(self):
		print(".........这是一辆索纳塔...........")

class No(Car):
	def info(self):
		print("此车型工厂尚未生产")
class Mingtu(Car):
	def info(self):
		print(">>>>>>这是一辆名图<<<<<<<<<<")

class factory():#工厂类
	#@staticmethod#静态方法--类对象可以直接调用
	def generate(self,car_type):
		if car_type == "索纳塔":
			return Suonata ()
		elif car_type == "名图":
			return Mingtu()
		else :
			return No()


class CarStore(object):#4s店类
	def __init__(self):
		self.factory = factory()#指定工厂
	def order(self,car_type):
		return self.factory.generate(car_type)#将订单交给工厂类中的生产方法中



car_store = CarStore()
car = car_store.order("索纳塔")
car.info()
#car.move()
#car.music()