# In every class there will be many properties
# and very few properties are common to all the objects
# Its good to keep these properties at the class level
# rather than keep at the object (instance) level
class Participant:
    # assuming all these participants are going to take
    # one particular program "Python Data Science / Machine Learning"
    # Class variables are inside the class but outside the methods
    # Class variables will be detroyed when the class is destroyed
    # To access the class variable we will use the Class as prefix
    course = "Python Data Science / Machine Learning"

    def __init__(self, firstname, lastname):
        # the following properties will be created at the
        # object level. In other words every object being
        # created will allocate space to keep these values
        self.firstname = firstname
        self.lastname = lastname
        count = 1
        print(self.firstname, self.lastname, count)
        # inside the methods we can have 2 types of variables
        # 1) Instance variable prefix with the word self
        # Instance variable live until the object is destroyed
        # 2) Local variable not prefixed with the word self
        # Local variable will die after the method execution
        # Local variable created inside the method

    def getFullName(self):
        print(self.firstname, self.lastname)

khairi = Participant("Khairi", "Abu Bakar")
# when will the firstname, lastname detroy from memory
# when you destroy khairi firstname, lastname will be destroy
# del khairi

# when you want to access the instance variable you must prefix 
# with object
print(khairi.firstname)

# when you want to access the class variable you must prefix 
# with Class
print(Participant.course)