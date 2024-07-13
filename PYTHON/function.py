print("Hello World !!!")

# Can i just use print function as above

# Or do I have to create a function place this code
# inside the function and call the function ?
# How many places are you going to have this line of code
# more than 1 time it must be converted to a function

# declaring a function
# def is the keyword we use to declare a function
# function must have a name following the def keyword
# the function name is followed by parenthesis ()
# again which is followed by colon :
# the code which is suppose to be inside the function
# must have indentation
def sayHelloWorld():
    print("Hello World !!!")

# how to call or invoke a function
# use the function name followed by parenthesis ()
# what will happen if we did not call/invoke a function ?
# Nothing python will not say anything
# But the function is a waste
sayHelloWorld()

# some function require some input
# or a variable  or a place holder to keep the input
# that is called "Parameter"
# name is a parameter
def greeting(name):
    print("Good Morning", name)

# since the function requires input you must pass value
# the value is called "Argument"
# John is argument
greeting("John")

# let us create a function that takes more than one parameter(s)
def calculateSimpleInterest(principle, period, rate):
    interest = (principle * period * rate) / 100
    print(interest)

# let us call/invoke the function by passing more than one argument(s)
# However the number of argument(s) must be same as number of parameter(s)
# the arguments are positional
calculateSimpleInterest(1000, 1, 6)
rate = int(input("Please key in interest: "))
calculateSimpleInterest(1000, 2, rate)
calculateSimpleInterest(1000, 3, 5)

# context
def buylunch(makan, minum):
    total = 0
    packedfood = []
    for food in makan:
        packedfood.append(food)
        if (food == "nasi"): total = total + 2.20
        if (food == "sayur"): total = total + 2.80
    for food in minum:
        packedfood.append(food)
        if (food == "nescafe"): total = total + 3
        if (food == "air warm"): total = total + 0.50
    # you can return a single value
    # return total
    # you can return multiple values
    return [packedfood, total]
    # code after the return never get executed
    print("thank you")

# context => Caller context
result = buylunch(["nasi", "sayur"], ["nescafe", "air warm"])
result = result[1] + .5
print("Amount to be Paid: ", result)

# can i have more than one return statement inside the function
# yes you can have more than one return statement
# however, you must remember once the return statement is executed 
# it will come out of the function
def evenOrOdd(givenNumber):
    if (givenNumber % 2 == 0):
        return "Even Number"
        print("It will not get executed")
    else:
        return "Odd Number"
        print("It will not get executed")
    
print(evenOrOdd(5))
print(evenOrOdd(6))

# Whenever python requires to convert the collection of data it will always use tuple
def returnNumbers():
    # function cannot return more than 1 value
    # in this case python will automatically return tuple of 5 numbers
    return 10, 20, 30, 40, 50

print(returnNumbers())

# function context
def calculateTotal(numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total

# caller context
# number of arguments is keep changing
# "Variable Length Arguments"
# Tranditionally how we handle such problem is using list
print(calculateTotal([10, 20, 30, 40, 50]))
print(calculateTotal([10, 20, 30, 40, 50, 60, 70]))
print(calculateTotal([10, 20, 30, 40, 50, 60, 70, 80, 90]))

# however, now we have a problem where the caller context cannot send the value
# in a list
# In python to handle variable length argument problem they introduce something
# called *parameter
# When python sees * it will convert all the arguments to a tuple and pass the
# tuple to the function
# again the point is whenever python has to convert a collection it will use tuple
def findTotal(*numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total

print(findTotal(10, 20, 30, 40, 50))
print(findTotal(10, 20, 30, 40, 50, 60, 70))
print(findTotal(10, 20, 30, 40, 50, 60, 70, 80, 90))

def findTotalByTuple(numbers):
    # tempnumbers = numbers.copy()
    total = 0
    for number in numbers:
        total = total + number
    # numbers[2] = 35
    # tempnumbers[2] = 35
    return total

data = [10, 20, 30, 40, 50]
# convert the list to a tuple
# data = tuple(data)
print(findTotalByTuple(tuple(data)))
print(data)

# create a function that takes 3 parameters
# and return single value
# however i dont want to pass the period and rate
# principle is the one always change
# you can make the parameters as optional by setting a default value
def calculateSI(principle, period=1, rate=6):
    interest = (principle * period * rate) / 100
    return interest

print(calculateSI(1000, 2, 5))
print(calculateSI(1000, 2))
print(calculateSI(1000))

# In python we have something called keyword argument
print(calculateSI(rate=5, principle=1000))

print("Hello", "Jegan", "Welcome", "to", "Python", sep="***", end="")
print("World")

# def print(*data, sep=" ", end="\n"):
    # input("hello")

# Remember when we call a function
# function(values) => we call the values as arguments

def add(a, b):
    return a + b

print(add(10, 20))
# Can we say add(10, 20) is an argument to function print ?
# NO
# Whenever a function is followed by () it gets executed first
# In this case the add function is executed first which returns 30
# The number 30 becomes the argument for print function

def minus(a, b):
    return a - b

# Let us create a common function which will be called by user
# to perform all arithmetic operation(s)
"""
def arithmetic(keyword, a, b):
    if (keyword == "add"): 
        return add(a, b)
    elif(keyword == "minus"):
        return minus(a, b)
"""
def arithmetic(func, a, b):
    return func(a, b)

# the caller is suppose to pass the function instead of keyword
# print(arithmetic("add", 10, 20))
print(arithmetic(add, 10, 20))

def multiplication(a, b):
    return a * b

# print(arithmetic("mul", 10, 20))
print(arithmetic(multiplication, 10, 20))
