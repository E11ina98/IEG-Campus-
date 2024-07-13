# if we want to use any of the built in python module
# then we have to import them inside our program and use it

import sys

print(sys.argv)

for value in sys.argv:
    print(value)

print(len(sys.argv) -1)   #use len for how many item in the list

# we want to perform and addition of all the arguments
total=0
for value in sys.argv[1:]:
    total = total + (int(value))

print("Total:" ,total)

#Parsing




