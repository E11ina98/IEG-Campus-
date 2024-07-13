# input is a built in function
# which takes a single parameter (caption/question)
# The input function displays the caption to the user 
# and wait for the keyboard input 
# user will provide the input and press enter key
# the input is always "string"
# the string value is assigned to the variable

firstNumber= input(" Enter the first number: ")
secondNumber= input(" Enter the second number: ")
print(firstNumber)
print(type(firstNumber))

# if you want to perform arithmatic opertion 
# this must be converted to a number
firstNumber= int (firstNumber)
secondNumber=int( input(" Enter the second number: "))

print( firstNumber + secondNumber)