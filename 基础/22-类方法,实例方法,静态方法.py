class Game():
	num = 0 #类属性

	def __init__(self):#实例方法(self)
		self.name = "laowang"
		Game.num = 3
	@classmethod #类方法
	def add_num(cls):
		cls.num = 100


	@staticmethod#静态方法
	def print_menu():#没有参数
		print(">>>>>>>>>>>>>")	

game = Game()
print(game.name)
#Game.add_num()#类对象调用类方法
game.add_num()#实例对象调用类方法
print(Game.num)
print(game.num)#实例对象调用类属性会复制出一个同名实例属性
game.num = 5	#更改的是实例属性
print(Game.num)
print(game.num)
Game.print_menu()#静态方法调用
game.print_menu()

































