x = 10

# Syntax Error
#if (x%2==0):
#print("Even Number")

# Logical Error
#if (x % 2 == 0):
#   print(f"Given Number is {x}")
#print("Even Number")


try:

# Runtime Error
# WE KNOW the folloWing line is taking user input
# in future this may throw error
# try except
# another example put the file open code here
    principle = int( input("Principle"))  

except ValueError:
    # the code inside the except bllock will get executed
    # only when an error occurs
    # another example put the file errors like file corripted/ file missing/ permission denied
    print("Principle amount must be an integer")
    #principle = 10000

except Exception as e:          #=> always captured any error
    print ("Something went  wrong:" ,e)

else:
    # the code inside  the else block get executed 
    # #only when therre is no error
    print("All is well")

finally:
    # the code inside this finally block will always gets executed
    # regardless of wether an error occur or not
    # another example Close the file
    print("Thank you")
    


# the program does not get terminated abnormally

period = int(input("Period"))
rate = int(input("Rate"))
interest = (principle * period * rate) /100
print("Interest Amount:" , interest)


# Note
# make sure error system is very friendly

