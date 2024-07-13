import datetime
from os.path import exists

def keyboardInput(datatype, caption, errorMessage):
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
        print("\nCar Management System")
        print("1. List all cars")    
        print("2. Add a new car")
        print("3. Edit an existing car")
        print("4. Remove a car")
        print("5. Check pending road tax renewals")
        print("6. Update car price")
        print("7. Exit")
        choice = keyboardInput(int, "Choice must be Integer")

        if choice == '1':
            listCar(filename)
            print("\nListing all cars:")

        elif choice == '2':
            addCar(filename)
            print("Car added successfully!")

        elif choice == '3':
            editCar(filename)
            print("Car edited successfully!")

        elif choice == '4':
            removeCar(filename)
            print("Car removed successfully!")

        elif choice == '5':
            pending_roadtax_renewal(filename)

        elif choice == '6':
            updateCar(filename)
            print("Car price updated successfully!")

        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

filename = "cars.txt"

def createFile(filename):
    if not exists(filename):
        try:
            filehandler = open(filename, "xt")
        except Exception as e:
            print("Something went wrong when we create the file:", e)
        else:
             createTitle(filename)
        finally:
            filehandler.close()

def createTitle(filename):
    try:
        with open(filename, 'wt') as filehandler:
            filehandler.write("Make|Model|Year|Roadtax Expiry|VIN|Cost Price|Current Price|Status")
    except Exception as e:
            print("Something went wrong when we create the title:", e)
    finally:
            filehandler.close()

def addCar(filename):
    try:
        make = keyboardInput(str, "Make: ", "Make must be string")
        model = keyboardInput(str, "Model: ", "Model must be string")
        year = keyboardInput(int, "Year: ", "Year must be int")
        roadtax_expiry= keyboardInput(str, "RoadTax Expiry: ", "RoadTax must be string")
        vin = keyboardInput(str, "VIN: ", "VIN must be string")
        cost_price= keyboardInput(float, "Price: ", "Price must be float")
        current_price= keyboardInput(float, "Current Price: ", "Current Price must be float")
        status = keyboardInput(str,"Car status: ","The input invalid.")

        with open(filename, "at") as filehandler:
            filehandler.write(f"\n{make}|{model}|{year}|{roadtax_expiry}|{vin}|{cost_price}|{current_price}|{status:>15}")
    except Exception as e:
        print("Something went wrong when we append the product:", e)

def listCar(filename): #==> list
    try:
        with open(filename, "rt") as filehandler:
            lines = filehandler.readlines()
        for index, line in enumerate(lines):
            make, model, year, roadtax_expiry,vin,cost_price,current_price,status = line.strip().split("|")
            if (index == 0):
                print("=" * 80)
            else:
                print(f"{index:<5}{make:20}{int(model):>20}{float(year):>20}{roadtax_expiry:20}{int(vin):>20}{float(cost_price):>20}{float(current_price):>20}{status:>15}")
    except Exception as e:
        print("Something went wrong when we print the products", e)

def editCar(filename):
    try:
        with open(filename, "rt") as filehandler:
            lines = filehandler.readlines()
        data = [line.strip().split("|") for line in lines]

        print("=" * 80)
        print(f"{'No':<5}{'Make':<20}{'Model':<20}{'Year':<10}{'Roadtax Expiry':<15}{'VIN':<20}{'Cost Price':<15}{'Current Price':<15}{'Status':<10}")
        print("=" * 80)
        for index, line in enumerate(data):
            if index == 0:
                continue
            make, model, year, roadtax_expiry, vin, cost_price, current_price, status = line
            print(f"{index:<5}{make:<20}{model:<20}{year:<10}{roadtax_expiry:<15}{vin:<20}{cost_price:<15}{current_price:<15}{status:<10}")

        index = keyboardInput(int, "Index of car to edit: ", "Index must be an integer")
        if index >= len(data) or index == 0:
            print("Sorry, not available :(")
        else:
            make, model, year, roadtax_expiry, vin, cost_price, current_price, status = data[index]
            print(f"Make: {make}\nModel: {model}\nYear: {year}\nRoad Tax Expiry: {roadtax_expiry}\nVIN: {vin}\nCost Price: {cost_price}\nCurrent Price: {current_price}\nStatus: {status}")
            confirm = keyboardInput(str, "Are you sure? (y/n): ", "Incorrect response")
            if confirm.lower() == "y":
                newMake = keyboardInput(str, f"Make [{make}]: ", "Make must be a string") or make
                newModel = keyboardInput(str, f"Model [{model}]: ", "Model must be a string") or model
                newYear = keyboardInput(int, f"Year [{year}]: ", "Year must be an integer") or year
                newRoadtax = keyboardInput(str, f"Road Tax Expiry [{roadtax_expiry}]: ", "Road Tax Expiry must be a string") or roadtax_expiry
                newVin = keyboardInput(str, f"VIN [{vin}]: ", "VIN must be a string") or vin
                newCostprice = keyboardInput(float, f"Cost Price [{cost_price}]: ", "Cost Price must be a float") or cost_price
                newCurrentprice = keyboardInput(float, f"Current Price [{current_price}]: ", "Current Price must be a float") or current_price
                newStatus = keyboardInput(str, f"Status [{status}]: ", "Status must be a string") or status
                data[index] = [newMake, newModel, newYear, newRoadtax, newVin, newCostprice, newCurrentprice, newStatus]

                with open(filename, "wt") as filehandler:
                    for line in data:
                        filehandler.write("|".join(map(str, line)) + "\n")
                print("Car edited successfully!")
    except Exception as e:
        print("Something went wrong when we edited the car:", e)

def removeCar(self):
        pass

def pending_roadtax_renewal(filename):
    try:
        current_date = datetime.datetime.today().date()
        with open(filename, "rt") as filehandler:
            lines = filehandler.readlines()
        data = [line.strip().split("|") for line in lines]

        print("Pending road tax renewals:")
        for index, line in enumerate(data):
            if index == 0:
                continue
            make, model, year, roadtax_expiry, vin, cost_price,current_price, status = line
            roadtax_expiry_date = datetime.datetime.strptime(roadtax_expiry, "%d.%m.%Y").date()
            if roadtax_expiry_date < current_date:
                print(f"{index:<5}{make:<20}{model:<20}{year:<10}{roadtax_expiry:<15}{vin:<20}{cost_price:<10}{current_price:>20}{status:<10}")
    except Exception as e:
        print("Something went wrong when checking pending road tax renewals:", e)

def updateCar(self):   # tambah current price + lst price
       pass


filename = "cars.txt"
createFile(filename)
#doMenu(filename)
#addCar(filename)
#listCar(filename)
pending_roadtax_renewal(filename)
#editCar(filename)

