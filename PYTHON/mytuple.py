# Tuple is a data structure / sequence
# Tuple is nothing but read only list
# Tuple is denoted using round bracket ()
# Tuple allow duplicates
# Tuple is not modifiable
# Tuple is ordered (the items inside the list retain its position)
# Tuple is indexed (0, 1, 2, 3, 4, 5......)
# Data inside the tuple is heterogeneous the data can be of different types

fruits = ("apple", "orange", "mango", "banana")
print(type(fruits))
print(fruits)

# Indexing and Selection
# print(fruits[0])
# Please refer variablesparttwo.py

# Tuple is not modifiable
# append, remove, pop, del
# del fruits[0] # cannot delete item
del fruits # you can always delete the entire tuple

# since tuple has less methods obviously
# 1) It take less memory
# 2) It is faster than list
# Normally when we do data processing we will convert the list to a tuple
# But whenever you require to do changes then you must keep it as list

# there is one feature which list and tuple has
# auto explode
fruits = ("apple", "orange", "mango")
fruit01 = fruits[0]
fruit02 = fruits[1]
fruit03 = fruits[2]
print(fruit01, fruit02, fruit03)
# the above is manual explode
# However you no need to do this in python list
fruit01, fruit02, fruit03 = fruits
print(fruit01, fruit02, fruit03)
# this is the second instance we are having more than 1 variable in the left hand side

# In tuple we have one problem
x = (10) # we are trying to assign a tuple with 1 item 10
# python will interpret this as expression that returns single value
print(x)
print(type(x))

x = (10,)
print(x)
print(type(x))
            




