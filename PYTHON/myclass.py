# principle = 1000
# period = 1
# rate = 6
# simpleInterest = (principle * period * rate) / 100
# print("Simple Interest:", simpleInterest)

"""
def calculateSimpleInterest(principle, period, rate):
    simpleInterest = (principle * period * rate) / 100
    return simpleInterest

def calculateTotalAmountToBePrinted(principle, simpleInterest):
    return principle + simpleInterest

principle = 1000
period = 1
rate = 6
result = calculateSimpleInterest(principle, period, rate)
newresult = calculateTotalAmountToBePrinted(principle, result)

print("Simple Interest:", result)
print("Total amount to be paid:", newresult)
"""

# Class is a blue print
# which contains variables and functions inside the class
# However the variables inside the class is called properties
# the functions inside the class is called methods
class Student:
    
    # In python we cannot declare properties (variabels)
    # without assigning a value
    # There is a special method (function) called constructor

    # This method gets called/invoked/executed 
    # everytime when you create an object 
    # of this class (instance of this class)
    
    # Since it is a special method it must have double underscore
    # followed by init and again followed by double underscore
    # Difference between a method and a function
    # 1) Method is nothing but a function inside a class
    # 2) Methods will have atleast 1 parameter
    # 3) You no need to pass argument for the first parameter
    # 4) First parameter of the method is very special
    # 5) Value for tha parameter is handle by python itself
    # 6) Usually that parameter is called self
    def __init__(self):
        print("Object is created")

    # This is our first method/function inside the class Student
    # remember methods must have atleast 1 parameter
    def attendClass(self):
        print("Object started attending the class")

    def doProject(self, projectname):
        print("Object started doing the project:", projectname)

    def attendExam(self, exam):
        grade = "A"
        return f"Object has attended the exam: {exam} and obtained the score {grade}"

# let us create our first object
zul = Student()
# how to invoke/call the method ?
# since the method has single parameter and the first parameter
# will be handle by python we no need to pass any argument
zul.attendClass()
# since the method has 2 parameters and the first parameter
# will be handle by python we no need to pass argument for the first
# parameter but we must pass argument for the second parameter(projectname)
zul.doProject("Pokemon")
print(zul.attendExam("Python 102"))