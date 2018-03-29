class Money(object):
	def __init__(self,money):
		self.__money = money

	@property
	def money(self):
		return  self.__money

x = Money(100)
print(x.money)
