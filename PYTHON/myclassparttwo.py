class Student:

    # Usually init method is used to declare properties    
    # Difference between the variables and propertis
    # 1) Properties are nothing but varibles but inside the class
    # 2) Properties are always prefix by the first parameter
    # 3) If you did not declare with prefix the that will become
    # just a local variable inside the method
    
    # Some of these properties are compulsory
    # You cannot become a student without telling your firstname,
    # lastname and icnumber
    # In other words you should not allow the object to be created
    # without value for these compulsory properties
    # however the program and address can be provided later (not compulsory)
    # we must take the compulsory values as parameter at the constructor
    def __init__(self, firstname, lastname, icnumber):
        self.firstname = firstname
        self.lastname = lastname
        self.icnumber = icnumber
        self.program = ""
        self.address = ""

    def attendClass(self):
        print(f"{self.firstname} {self.lastname} started attending the class")

    def doProject(self, projectname):
        print(f"{self.firstname} {self.lastname} started doing the project:", projectname)

    def attendExam(self, exam):
        grade = "A"
        return f"""{self.firstname} {self.lastname} has attended the exam: {exam} and obtained the score {grade}"""
    
    def info(self):
        print("First Name:", self.firstname)
        print("Last Name:", self.lastname)
        print("IC Number:", self.icnumber)
        # here program is a local variable created inside the method
        for program in self.program:
            print("Program:", program)
        print("Address:")
        print(self.address["Street"])
        print(self.address["Area"])
        print(self.address["Postcode"])
        print(self.address["State"])
        print(self.address["Country"])

    # there is also another special method
    # which returns string value
    # this method will be called whenever you try to print the object
    def __str__(self):
        return f"""First Name: {self.firstname}
        Last Name: {self.lastname}
        IC Number: {self.icnumber}"""

# how can we set value for the properties
# 1) Using constructor (__init__ method)
zul = Student("Ahmad", "Zul", "000102121234")
zul.attendClass()
zul.doProject("Pokemon")
print(zul.attendExam("Python 102"))
# 2) you can set values to the property directly using the dot operator
zul.program = ["Python", "Data Science", "Machine Learning"]
zul.address = {
    "Street": "15 Jalan SS2",
    "Area": "Subang Jaya 2",
    "Postcode": 43100,
    "State": "Selangor",
    "Country": "Malaysia"
}
zul.info()
# Default behaviour is to print the addres location where the object is
# However if we want to "override" that behaviour we can do that by
# creating a special method __str__
print(zul)
# when we try to print the object using print function 
# if that class has __str__ method it will be executed automatically