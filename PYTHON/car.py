#from datetime import datetime

from os.path import exists

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

def doMenu(filename):
    choice = -1
    while choice != 0:
        print("-----------")
        print("0  -  Exit")
        print("1  -  List")
        print("2  -  Add")
        print("4  -  Edit")
        print("5  -  Pending Roadtax Renewal")
        print("6  -  Update")

        print("-----------")
        choice = keyboardInput(int, "Choice(0,1,2,3): ", "Choice must be Integer")
        if (choice == 0):
            print("Thnx")
        elif (choice == 1):
            addProduct(filename)
        elif (choice == 2):
            addProduct(filename)
        elif (choice == 3):
            editProduct(filename)

filename = "cars.txt"

"""
class Cms:
    
    def __init__(self,make,model,year,color,plate_number,vehicle_number):
        self.make = make
        self.model = model
        self.year = year
        self.color= color
        self.plate_number = plate_number
        self.vehicle_number = vehicle_number
"""       
def __str__(self):
        pass
def addCar(self):
        try:
            make = keyboardInput(str, "Product: ", "Product must be string")
            model = keyboardInput(int, "Quantity: ", "Quantity must be interger")
            price = keyboardInput(float, "Price: ", "Price must be float")
            with open(filename, 'at') as filehandler:
                filehandler.write(f"\n{product}|{quantity}|{price}")
        except Exception as e:
            print("Something went wrong when we append the product:", e)
            pass
        
def editCar(self):
        pass

def removeCar(self):
        pass
def pending_roadtax_renewal(self):
        pass
def updateCar(self):
        pass

def createFile(filename):
        if not exists(filename):
            try:
                filehandler = open(filename, "xt")
            except Exception as e:
                print("Something went wrong when creating the file:", e)
            #else:
                #createTitle(filename)
            finally:
                filehandler.close()
    
def createTitle(filename):
        try:
            with open(filename, 'wt') as filehandler:
                filehandler.write("Product|Quantity|Price")
        except Exception as e:
            print("Something went wrong when creating the title:", e)



