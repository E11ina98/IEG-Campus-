# Aida
# any / all
# They are builtin functions
# they take boolen list as parameter
# [True, True, False]
# Any true become true
# if all function take the above list as parameter it will return false
# all requires everything to be true (all == and)
# check whether the given number is a prime number

givenNumber = 11
divisors= range(2,givenNumber) # =>list

# a list is given and we are going to create another list

if (len([mynumber for mynumber in divisors if (givenNumber % mynumber == 0)]) ==0):
    print ("Prime Number")
else:
    print("Not Prime Number")

if any([givenNumber % mynumber == 0 for mynumber in divisors]):
    print ("Not Prime Number")
else:
    print ("Prime Number")

# Prime Number
# check the given numebr is prime or not
# check the input is prime or not
# generate first 10 prime numbers between 10 to 100