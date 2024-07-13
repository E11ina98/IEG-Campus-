from classq2Address import classq2Address

class classq2Person:
	
	def __init__(self,name, age, address):
		self.__name = name
		self.__age = age
		self.__address = address
	
	def __str__(self):
		return f"{self.__name} is a person who is {self.__age} years old and lives in the following address : {self.__address}"
		
