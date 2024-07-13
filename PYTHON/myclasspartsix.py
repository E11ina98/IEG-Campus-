# Polymorphism

class Gender:
    def __init__(self):
        pass
    def doCarryObjects(self):
        pass

class Male(Gender):
    def __init__(self):
        pass
    def doCarryObjects(self):
        print("Carry Heavy Objects")

class Female(Gender):
    def __init__(self):
        pass
    def doCarryObjects(self):
        print("Carry Light Objects")

def getGender(name):  #==> ni function bkn method xde self
    if "A/L" in name:
        return Male()
    else:
        return Female()
    

# Python dynamically set the data type for the gender variable
# sometimes it becomes Male object 
# sometimes it becomes Female object
gender = getGender("Khairi A/L Abu Bakar")
gender.doCarryObjects()
print(type(gender))

gender = getGender("Aida A/L Abu Bakar")
gender.doCarryObjects()
print(type(gender))