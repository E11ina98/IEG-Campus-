# only in python the function can access the variable
# declared in the main context

x = 10
def sayX():
    x = 0
    print(x) # usually x is initialized and then only used
    # in this case "function can see x"

sayX()

def modifyX():
    x = 20
    # whenever you modify the variable which is in the global context
    # the variable is initialized locally
    # in this case x automatically become local variable
    print(x)

modifyX()
print(x)

# what if i dont want to create x as local variable
# .....

def changeX():
    global x # telling python for variable x refer the main context

    x=20
    print(x)

modifyX()
print(x)
# Summary: Since I use the g lobal keyword inside my function
# my function is able to to change the value of x which is in global context

def authenticate():
    result = 11111
    def simpleInterest():
        nonlocal result
        result = 22222
        print(result)
    simpleInterest()
    print(result)
    


authenticate()