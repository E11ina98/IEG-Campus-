# Arithmatic Operators
# Addition / Subtraction / Multiplication / Division / Exponent
x = 7
y = 2
# expressions can be passed to print function
# in this case expression is an argument to print function
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Quotient:", x // y)
print("Remainder:", x % y)

# how to find exponent
# 10 x 10 x 10
print(10 ** 3)
# what is the maximum number a 64 bit can have
print((2 ** 64) - 1)

# Assignment Operators
x = 100 # we assign 100 to x
x += 1 # x = x + 1
x += 2 # x = x + 2
x += 5 # x = x + 5

# Fadhli Equation
x += x + 1 # x = x + (x + 1)
# x = 108
# x = 108 + 109 = 217
print(x)

x -= 1 # x = x - 1
print(x)

x *= 1 # x = x * 1
print(x)

x /= 1 # x = x / 1
print(x)

x //= 5 # x = x // 5
print(x)

x %= 5 # x = x % 5
print(x)

# Comparission Operator

myheight = 5.2
yourheight = 5.3
mybrotherheight = 5.2

# let us create TRUE statements
print(myheight < yourheight)
print(yourheight > myheight)
print(myheight == mybrotherheight)
print(myheight != yourheight)
print(myheight <= mybrotherheight) # less than or equals to
print(myheight <= yourheight) # less than or equals to
print(mybrotherheight >= myheight) # greater than or equals to
print(yourheight >= myheight) # greater than or equals to

# Logical operator
# It actually help us to solve more than one condition
# and: both/all conditions must be True
# or: any one of the condition is True
a = 10
b = 7
c = 4

# let us create TRUE statements
print(a > b and a > c) # True means a is the biggest number
print(c < a and c < b) # True means c is the smallest number

print(a > b or a > c) # True means 
# a can be bigger than b, a can be bigger than c and also
# a can be bigger than b and c

print((b < a and b > c) or (b > a and b < c)) # True b is the middle number

# Negation operator
isAvailable = True
print(not isAvailable)
print(not not isAvailable)

# sometimes we will have some statement to be executed
# when the condition fails (false) but we do not have any statement to be
# executed when the condition is true
# if (condition == true)
#    nothing to do
# else
#   got something to do

# if (not condition == true)
#   got something to do

myheight = 5.2
yourheight = 5.3

print(not myheight > yourheight) 
# because we have not infront the result False becomes True
# that is why not is called negation operator

