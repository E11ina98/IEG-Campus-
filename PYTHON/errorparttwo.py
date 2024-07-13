def keyboardInput(datatype,caption, errorMessage):
    value = None
    isInvalid = True
    while (isInvalid):
        try:
            value = datatype(input(caption))
        except: 
            print(errorMessage)
        else:
            isInvalid = False
    return value


def calculateSimpleInterest():
    principle = keyboardInput(int, "Principle amount:", "Principle Amount must be Integer")
    period = keyboardInput (float,"Period in years:", "Period must be Float")
    rate = keyboardInput (float, "Rate in percentage:", "Rate must be float")
    interest =  (principle * period * rate) /100
    print("Interest Amount:", interest)
    print("Total Amount to be paid" , principle + interest)

calculateSimpleInterest()

#mylist  = ['1','2','3']
#map(int, mylist)