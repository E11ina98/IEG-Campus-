fruits = ["apple", "rambutan", "orange", "durian", "mango", "papaya", "banana", "grapes"]

# to print all the fruits in the list
for fruit in fruits:
    print(fruit)

# print the fruit which is in the even position
for fruit in fruits[::2]:
    print(fruit)

# print the fruit that has 6 characters
for fruit in fruits:
    if (len(fruit) == 6):
        print(fruit)

multiplicants = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
multiplier = 5
for multiplicant in multiplicants:
    print(multiplicant, "x", multiplier, "=", multiplicant * multiplier)

# range operator : will not generate list of numbers
# it is used to select from a list 
# however we have a function called range
# range function will help us to generate number 
# range function takes start_index, end_index
# start_index is included
# end_index is not included
multiplicants = range(1, 13)
multiplier = 6
for multiplicant in multiplicants:
    print(multiplicant, "x", multiplier, "=", multiplicant * multiplier)

# products = ["cooking oil", "ginger", 'garlic', 'tomato', 'milk']
# go to the super market
# for product in products:
#    shelfno = search(product)
#    walkto(selfno)
#    if notsure():
#       callwife(question)
#       product = product + "10kg"
#    pick(product)
#    addtocart(product)
# checkout(mycart)
# total = 0
# for product in mycart:
#    price = getprice(product)
#    total = total + price
#    addtobasket(product)
# dopayment(total)

# Take a number as input print all the digits in the number
usernumber = int(input("Enter the number: "))
# mynumber = 12345
# do you have a list = no
# how many digits do we have = dont know
# you have to use while loop
mynumber = usernumber
print("-----------------------")
while(mynumber > 0):
    print(mynumber % 10)
    mynumber = mynumber // 10

mynumber = usernumber
print("-------------------------")
numberofdigits = len(str(mynumber)) - 1
while(mynumber > 0):
    print(mynumber // 10 ** numberofdigits)
    mynumber = mynumber % 10 ** numberofdigits
    numberofdigits = numberofdigits - 1

mynumber = str(usernumber)
print("-------------------------")
for number in mynumber:
    print(number)

# Hanafi Effect
num = str(usernumber)
i = 0
while i < len(num):
    print(int(num[i]))
    i += 1


fruits = ["apple", "rambutan", "orange", "durian", "mango", "papaya", "banana", "grapes"]
# Only in python the for loop can have else part
# The code in the else part will get executed only when all the fruits are iterated fully
# The iteration is exhausted (there is nothing else lah to read)
for fruit in fruits:
    print(fruit)
    # if fruit == "durian": break
else:
    print("All fruits are printed")

# Generate first 10 prime number
for mynumber in range(2, 51):
    for divisor in range(2, mynumber):
        if (mynumber % divisor == 0): break
    else:
        print(mynumber, "is prime number from for loop")

# Only in python the while loop can have else part
# The code in the else part will get executed only when the condition fails
# the condition in the while loop must return FALSE
count = 10
givennumber = 2
while count > 0:
    for divisor in range(2, givennumber):
        if (givennumber % divisor == 0): break
    else:
        count -= 1
        print(givennumber, "is prime number")
        # because of the break keyword we leave the while loop 
        # after printing the 5 prime numbers
        # which make the condition still TRUE but we get out of the Loop
        if givennumber > 10: break
    givennumber += 1
else:
    print("10 prime number are printed")


# continue keyword
multiplicants = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
multiplier = 7
for multiplicant in multiplicants:
    if multiplicant % 5 == 0: continue
    # continue the loop without executing the following statements
    print(multiplicant, "x", multiplier, "=", multiplicant * multiplier)
