# HAS-A retlationship
# Customer has a passport
class Passport:               

    def __init__(self,country,passportnumber):
        self.country  = country
        self.passportnumber = passportnumber

    def __str__(self):
        return f"Country: {self.country} \n Passport Number: {self.passportnumber}"

class Customer:

    def __init__(self,firstname, lastname):
        self.firstname= firstname
        self.lastname = lastname
        self.icnumber = " "
        # customer has a passport
        # when you have has-a relationship with another class then that
        # ...
        self.passport = None

    def __str__(self):
        message= f"First Name: {self.firstname}\n"
        message= message + f"Last Name: {self.lastname}\n"
        message= message + f"IC Number: {self.icnumber}\n"
        if(self.passport != None):
            message = message + self.passport.__str__()
        return message

peter = Customer("Parker", "Peter")  
passport = Passport("UK", "E0202932")
peter.passport = passport
print(peter)
# now we know how to convert an python object to a dictionary
print(peter.__dict__)
