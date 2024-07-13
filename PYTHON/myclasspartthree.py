# Encapsulation
# Encapsulate the properties inside the class
# in other languages we have keywords private,public,protected
# to protect the properties

class circle:
    
    def __init__(self,radius):
        # change the property with single underscore
        # this makes the property private
        self._radius = 0                 #self.radius ==> properties  # initialized the propoerties without any condition
        if (isinstance(radius,int)):
             self._radius= radius
        else:
            print("Invalid Radius")

    # getter method and setter method   => more secure
    def getRadius(self):
        return self._radius
    
    def setRadius(self,radius):
        if(isinstance(radius,int)):
            self._radius = radius
        else:
            print("Invalid Radius")
    
    # property is a clss
    # calling/invoking the class by passing method as argument
    # please notice after getRadius there is no ()
    # the property class returns the property object which is assigned to
    # a variable radius
    # in other words radius is an instance of property class
    radius = property(getRadius, setRadius) #=> create new property called radius

    def area(self):
        return  3.14 * self._radius * self._radius

    def circumference(self):
        return  2 * 3.14 * self._radius 
    
    def __str__(self):
        return f"Radius of this circle is {self._radius}"
    
mycircle = circle(20)
print(mycircle)
#mycircle = circle("abc")
#print(mycircle)

mycircle.radius = "abc"   # assessing properties directly
print(mycircle)
print(mycircle.area())
mycircle.radius = 30
print(mycircle)


# the value set in properties must be valid
