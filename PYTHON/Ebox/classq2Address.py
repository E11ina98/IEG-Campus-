class classq2Address:
	
	def __init__(self,street, city, state):
		self.__street = street
		self.__city = city
		self.__state = state
	
	def __str__(self):
		return (f"{self.__street}, {self.__city},{self.__state}")
		