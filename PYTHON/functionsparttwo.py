# 
# 2 things (1) parameter 2) return
# already know how to pass the argument

def authenticate(username, password):  #parent
    def simpleInterest (principle,period, rate): #child
        def something():  # grand child
            pass
        return (principle*period *rate) / 100
        
    if (username == "admin" and password == "pwd123"):
        # now we know funtion can have inner function
        # inner function can be called from the outer function
        # however you cannot call the inner function
        # from the main contecxt
       # print ("Interest Amount: " ,simpleInterest(1000,1,6))
       return simpleInterest
 


func = authenticate("admin", "pwd123")
print("Interest amount:", func(1000,1,6))


def sum(a,b):
    return a+b


#sum = def(a,b):
#   return a+b

x = 10
def sayX():
    print(x)

sayX()

#however python still has lambda function
# lambda function can have only one statement
def add (x,y):
    return x + y
# Step 1: convert your function to an annonymous function
# Step 2: we cannot call the no name functiom
# let us assign the function to a variable
#sum = def (x,y): return x =y
# step 3: rename drf with lambda
#sum = lambda (x,y): return x+ y
# step 4 : parenthesis "()" and "return" keyword can be remove

sum = lambda x,y: x+y

print(sum(10,20))

fahrenheitvalues = [32, 33, 34, 35, 36, 37, 38, 39, 40]
def convertFahrenheitToCelsius(fahrenheitvalue):
    return (fahrenheitvalue - 32) * 5/9
celciusvalues= map(convertFahrenheitToCelsius,fahrenheitvalues)
print(list(celciusvalues))

celciusvalues= map(lambda value:(value-32)*5/9,fahrenheitvalues)
print(list(celciusvalues))


prices = [10, 20, 30, 40, 50]
priceswithsst = []
for price in prices:
    priceswithsst.append(price + (price * 0.06))
print("Prices with sst using for loop:", priceswithsst)

priceswithsst= map(lambda value:(price + (price * 0.06)),prices)
print(list(priceswithsst))

