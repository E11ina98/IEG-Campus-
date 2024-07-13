

class calculator:
    def  __init__(self,x,y):
        self.x = x
        self.y = y

    def add (self):
        return self.x + self.y
    
    def substract (self):
        return self.x - self.y
    
mycalculator = calculator(20,10)
print(mycalculator.add())
print(mycalculator.substract())

class Utility: 

    def addition(x,y):
        return x+y
    
    def substraction(x,y):
        return x-y
    
print(Utility.addition (10,20))


class Customer:
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname

    def getfullname(firstname, lastname):
        return firstname + lastname
    
    def __str__(self):
        return Customer.getfullname(self.firstname, self.lastname)
    
myCustomer  = Customer("John", " David")
print(myCustomer)