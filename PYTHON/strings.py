firstname = "Khairi"
lastname = "Abu Bakar"
# + is arithmatic operator used for addition
# to perform addition both side of + must be integer or float

# however if both sides are string then python performs
# string concatenation
fullname = firstname + " " + lastname
print(fullname)

carplate = "JCG"
number = 9876
# in this case one is string (JCG) another one is number (9876)
# python does not know whether to perform addition or 
# string concatenation

# I can only concatenate str (not "int") to str
# JCG cannot be converted to number 
# 9876 can be converted to string
# we use the buit in function str to convert
carplatenumber = carplate + str(number)
print(carplatenumber)

# we also know * means multiplication
# how can we use * over string data
product = "book"
# when you multiply string with integer then the * becomes times operator
print(product * 5)
print("=" * 50)

# We already know string values (string literal) in python are enclosed 
# either with double quote "" or single quote ''

# How we handle multiline string traditionally
# slash \ is also called escape sequence
# When this slash is followed by some letter it has meaning
# \n = new line character
# \t = tab character
# \r = carriage return
content = "As I am not \t feeling well, \n"
content = content + "I am not able to \ attend the meeting, \n"
content = content + "Please proceed without \rmy presence\n"
print(content)

filepath = "c:\newfolder\table\readme.txt"
print(filepath)
# using escape sequence by adding \
filepath = "c:\\newfolder\\table\\readme.txt"
print(filepath)
# raw string
filepath = r"c:\newfolder\table\readme.txt"
print(filepath)

#Also remember/character is used to tell python the statement is not complete
# the continuation is in the next line
total= 2 + 3 + 4 +\
        5 + 6
print(total)

# However in python you can use """...""" or '''...'''
# to handle multiline strings
content = """As I am not feeling well,
I am not able to attend the meeting,
Please proceed without my presence"""

print(content)

"""
As I am not feeling well,
I am not able to attend the meeting,
Please proceed without my presence
"""

# Relationship between strings and list
# strings are nothing but list of characters
message = "Hello World" # ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
print(message[0])
print(message[0:5])
print(message[-5:])
print(message[::-1])

mynumber = 86749
# strmynumber = str(mynumber)
# print(int(strmynumber[::-1]))
print(int(str(mynumber)[::-1]))

numbers= input("Enter the numbers(comma separated): ")
print(numbers)
print(type(numbers))   #type is always string
values= numbers.split(",")
print(values)
print(type(values))

total=0
for value in values:
    total=total + int(value)
print(total)






