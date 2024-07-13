# product is the variable
# "Television " is the string value/ literal
# to diffrentiate between the variables and value are double quote "" or single quote''

product = "Television"   #string
quantity = 2             #integer
price = 1455.25          #float
available = True         # True or false (boolean value/literal)
print ("Product:", product)
print ("Quantity:", quantity)
print ("Price:", price)
print ("Available", available)


# type is another built in function that tells us what is the data type of the variables (dynamically assigned by python)
# data type of the variables (dynamically assigned by python)
# ((a + b)* c)
print (type(product))
print (type(quantity))
print (type(price))
print (type(available))

total =  quantity * price
print ("Total:", total)

# In real world use cases the 10 will not be hard coded
# the 10 is coming from an input device (keyboard)
# so the input value can be a string which needs to be converted 
quantity= "10"
print(type(quantity))
price= "1455.55"
 # print (quantity * price)

#type casting
#convert one data type to another
# to convert string to integer, we have to built in function int
# to convert string to float we have a built in function float
total = int(quantity) * float(price)
print(total)

firstNumber= 500
# how can i see the address where the object 500 is
# In python we have a built in function called "id"
print(id(firstNumber))
secondNumber = 500
print(id(secondNumber))

firstString= "Hello"
secondString= "Hello"
print(id(firstString))
print(id(secondString))

# so far we have seen how to assign one value to one variable
# in one line
# however we can also assign more than one value to more than 
# one variable in one line
x,y=1,2
print(x,y)

# how ever in python the following is not supported 
# x, y = 105
x,y=101 + 1,101 + 2
print(x,y)

#Initialization
x=0         #numeric initializer
x= " "      #string initializer
x= None     # no brain # no data type
print(type(None)) 




