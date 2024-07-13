# List is a data structure /  sequence
# list is denoted using square bracket []
# list allow duplicates
# list is modifiable
# List is ordered (the items inside the list retain its position)
# List is indexed (0,1,2,3.....)
# Data inside the list is heterogeneous
# the data can be of different types


# Let us create a list
fruits= ["apple", "orange", "mango","banana", "grapes"]
# fruits is variable, which can hold more than one value
# fruits is also an object, instance of List (class)
# Jegan, John are objects, instance of Human (class)
# Jegan has 2 eyes, 1 nose (properties)
# Jegan can walk, eat, run, teach, listen (methods) (what he can do)

quantity= [10,20,30,40,50]
# quantity is a variable, which can hold more than one value
# quantity is also called an object, which is intance of List (class)

# Indexing and Selection
# please refer to variablestwo.py

# You can add more items to the existing list
fruits.append("durian")
print(fruits)

# you can insert into existing list
# insert is another method we have in the list class
fruits.insert(1, "rambutan")
print (fruits)
fruits.insert(3, "cempedak")
print(fruits)

# how to modify an existing item
fruits[5] = "mangosteen"
print (fruits)

# how can i remove grapes
# remove is another method we have in the list class
fruits.remove ("grapes")
# however this will remove only the first instance of grapes
print(fruits)

# how can i remove an item using index
# there is no method to do this
# however we can use del keyword
# del keyword will delete any thing from memory permanently

del fruits[3]
print (fruits)

myname = "Jegan"
del myname
#print (myname)

# Clear all the items in the list
fruits.clear()
print(fruits)
del fruits
#print (fruits)

fruits = ["apple", "orange", "mango", "banana", "orange", "grapes"]
if ("orange" in fruits):
    print(fruits.index("orange"))
    print(fruits[fruits.index("orange")+1:].index("orange") + fruits.index("orange") + 1)
    # fruits.index("orange") => 1.........(1)
    # fruits.index("orange")+1: => 2:
    # fruits[2:] => ["mango", "banana", "orange", "grapes"]
    # fruits[2:].index("orange") => 2........(2)
    # 2 + 1 + 1

# you can also use built in function called enumerate
# enumerate is a function used to find index of every item in the list
enumeratedfruits = enumerate(fruits)
print(enumeratedfruits)
# enumerate object is also an iterable object
# in the for loop => for fruit in fruits
# fruits is a list 
# fruits must be iterable object
# however print function do not know how to iterate it so it prints the
# address location where the object is
# we can typecast any iterable object to a list 
# using a class list
fruitlist = list(enumeratedfruits)
print(fruitlist)
# the enumerated list is a list of tuples
# and each tuple has 2 values 
# 1) index
# 2) fruit (item)
for item in fruitlist:
    if (item[1] == "orange"): print(item[0])

# shallow copy
x = [10, 20, 30, 40, 50, 60, 70]
y = x
print(x)
print(y)
x[2] = 35
print(x)
print(y)

# deep copy
x = [10, 20, 30, 40, 50, 60, 70]
# y = x Don't do this
y = []
for i in x:
    y.append(i)
print("=" * 40)
print(x)
print(y)
x[2] = 35
print(x)
print(y)

# deep copy
x = [10, 20, 30, 40, 50, 60, 70]
y = x.copy()
print("=" * 40)
print(x)
print(y)
x[2] = 35
print(x)
print(y)

# x = 10
# x is a variable
# 10 is a literal
# when we assign 10 to x, x becomes an object
# since we assing 10 (integer), x becomes an object/instance of int class

# fruits = ["apple", "orange", "mango"]
# fruits is a variable
# ["apple", "orange", "mango"] is a literal (collection)
# when we assign ["apple", "orange", "mango"] to fruits, fruits becomes an object
# since we assign ["apple", "orange", "mango"] (list), fruits becomes and object/instance of list class

# product = "Television"
# product is a variable
# "Television" is a literal
# when we assign "Televison" to product, product becomes an object
# since we assign "Television" (string), product becomes an object/instance of string class

# here we are calling/invoking a class
# we are suppose to create an object by calling the class
# which returns an object fruits
fruits = list(["apple", "orange", "mango"])
# however in python they created this square [] syntax to create list
print(fruits)

# this parethesis () is really confusing
# we use () in expressions which returns single value (a + b * (c + d) / 100)
# to call/invoke anything in python we use the operator () round bracket
# to call/invoke a function print(), id(), 
# to create an object also range(), list(), tuple(), int(), floot()
# to call/invoke a method "television".split()
# to call/invoke a function inside a module sys.audit()
# to create tuple/datastructrue also we use (10, 20, 30, 40)

# there is one feature which list and tuple has
# auto explode
fruits = ["apple", "orange", "mango"]
fruit01 = fruits[0]
fruit02 = fruits[1]
fruit03 = fruits[2]
print(fruit01, fruit02, fruit03)
# the above is manual explode
# However you no need to do this in python list
fruit01, fruit02, fruit03 = fruits
print(fruit01, fruit02, fruit03)
# this is the second instance we are having more than 1 variable in the left hand side

                