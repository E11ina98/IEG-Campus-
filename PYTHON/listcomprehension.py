# list
fruits = ["apple", "orange", "mango", "banana"]
for fruit in fruits:
    print(fruit)

# overseafruits = fruits # we should not do this
# overseafruits = fruits.copy()

# We iterate through a list of values and we create a new list
# number of items in the newly created list is same as the original list

# iterate and create a new list
# then you can use something called "List comprehension"
# List + For Loop => List comprehension
# Instead of creating the tradional for loop we can do it using List comprehension
overseafruits = []
for fruit in fruits:
    overseafruits.append(fruit)
print("Copy using for loop:", overseafruits)

overseafruits = [fruit for fruit in fruits]
print("Copy using list comprehension:", overseafruits)

prices = [10, 20, 30, 40, 50]
priceswithsst = []
for price in prices:
    priceswithsst.append(price + (price * 0.06))
print("Prices with sst using for loop:", priceswithsst)

priceswithsst = [price + (price * 0.06) for price in prices]
print("Prices with sst using list comprehension:", priceswithsst)

# using a class called map
# it will return map object (interator)
# Step 1: convert the expression into a function
def calculateSST(price):
    return price + (price * 0.06)

# Step 2: use map class
# This is going to take 2 parameters
# 1st parameter is your function
# 2nd parameter is your list
priceswithsst = map(calculateSST, prices)
print("Prices with sst using map:", list(priceswithsst))

"""
def map(func, values):
    result = []
    for value in values:
        result.append(func(value))
    return result
"""

fahrenheitvalues = [32, 33, 34, 35, 36, 37, 38, 39, 40]
celsiusvalues = []
for fahrenheitvalue in fahrenheitvalues:
    celsiusvalues.append((fahrenheitvalue - 32) * 5/9)
print("Celsius Values using for loop:", celsiusvalues)

celsiusvalues = [(fahrenheitvalue - 32) * 5/9 for fahrenheitvalue in fahrenheitvalues]
print("Celsius Values using list comprehension:", celsiusvalues)

def convertFahrenheitToCelsius(fahrenheitvalue):
    return (fahrenheitvalue - 32) * 5/9

celsiusvalues = map(convertFahrenheitToCelsius, fahrenheitvalues)
print("Celsius Values using map:", list(celsiusvalues))


# We iterate through a list of values and we create a new list
# number of items in the newly created list is less than or same 
# as the original list
multiplesofthree = []
for number in range(0, 16):
    if (number % 3 == 0): multiplesofthree.append(number)
print("Multiples of three using for loop:", multiplesofthree)

multiplesofthree = [number for number in range(0, 16) if (number % 3 == 0)]
print("Multiples of three using list comprehension:", multiplesofthree)

def isMultipleOfThree(number):
    return True if (number % 3 == 0) else False
multiplesofthree = filter(isMultipleOfThree, range(0, 16))
print("Multiples of three using filter:", list(multiplesofthree))

numbers = [9, 4, 2, 3, 7, 6, 5, 11, 21, 18, 17, 27]
evennumbers = []
for number in numbers:
    if (number % 2 == 0): evennumbers.append(number)
print("Even numbers using for loop:", evennumbers)

evennumbers = [number for number in numbers if (number % 2 == 0)]
print("Even numbers using list comprehension:", evennumbers)

def isEven(number):
    return True if (number % 2 == 0) else False
evennumbers = filter(isEven, numbers)
print("Even numbers using filter:", list(evennumbers))

# We iterate through a list of values and we reduce it to a single value
numbers = [1, 2, 3, 4, 5]
total = 0
for number in numbers:
    total = total + number
print("Total using for loop:", total)

# Since we reduce the list to a single value we cannot use list comprehension

# However we can use another function called reduce (not builtin)
# which is inside a module called functools (builtin module)
from functools import reduce

numbers = [1, 2, 3]

def calculateTotal(previous, current):
    return previous + current

print("Sum using reduce:", reduce(calculateTotal, numbers))

"""
def reduce(func, values):
    sum = 0 
    # the reduce function is smart when you use multiplication
    # it initialze the sum with 1
    for value in values:
        sum = func(sum, value)
    return sum
"""
def calculateFactorial(previous, current):
    return previous * current

print("Factorial using reduce:", reduce(calculateFactorial, numbers))

# now the sum will be initialized with 5
print("Factorial using reduce:", reduce(calculateFactorial, numbers, 5))