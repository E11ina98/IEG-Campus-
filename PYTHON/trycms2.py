import datetime
from os.path import exists

def keyboardInput(datatype, caption, errorMessage):
    value = None
    isInvalid = True
    while isInvalid:
        try:
            value = datatype(input(caption))
        except:
            print(errorMessage)
        else:
            isInvalid = False
    return value

def doMenu(filename):
    choice = -1
    while choice != 7:
        print("\nCar Management System")
        print("1. List all cars")
        print("2. Add a new car")
        print("3. Edit an existing car")
        print("4. Remove a car")
        print("5. Check pending road tax renewals")
        print("6. Update car price")
        print("7. Exit")
        choice = keyboardInput(int, "Enter your choice: ", "Choice must be an integer")

        if choice == 1:
            listCar(filename)
        elif choice == 2:
            addCar(filename)
        elif choice == 3:
            editCar(filename)
        elif choice == 4:
            removeCar(filename)
        elif choice == 5:
            pending_roadtax_renewal(filename)
        elif choice == 6:
            updateCar(filename)
        elif choice == 7:
            print("Exiting...")
        else:
            print("Invalid choice, please try again.")


def createFile(filename):
    if not exists(filename):
        try:
            filehandler = open(filename, "xt")
        except Exception as e:
            print("Something went wrong when we created the file:", e)
        else:
            createTitle(filename)
        finally:
            filehandler.close()

def createTitle(filename):
    try:
        with open(filename, 'wt') as filehandler:
            filehandler.write("Make|Model|Year|Roadtax Expiry|VIN|Price|Status\n")
    except Exception as e:
        print("Something went wrong when we created the title:", e)

def addCar(filename):
    try:
        make = keyboardInput(str, "Make: ", "Make must be a string")
        model = keyboardInput(str, "Model: ", "Model must be a string")
        year = keyboardInput(int, "Year: ", "Year must be an integer")
        roadtax_expiry = keyboardInput(str, "Road Tax Expiry (YYYY-MM-DD): ", "Road Tax Expiry must be a string")
        vin = keyboardInput(str, "VIN: ", "VIN must be a string")
        price = keyboardInput(float, "Price: ", "Price must be a float")
        status = "Active"

        with open(filename, "at") as filehandler:
            filehandler.write(f"{make}|{model}|{year}|{roadtax_expiry}|{vin}|{price}|{status}\n")
        print("Car added successfully!")
    except Exception as e:
        print("Something went wrong when we added the car:", e)

def listCar(filename):
    try:
        with open(filename, "rt") as filehandler:
            lines = filehandler.readlines()
        for index, line in enumerate(lines):
            make, model, year, roadtax_expiry, vin, price, status = line.strip().split("|")
            if index == 0:
                print("=" * 80)
                print(f"{'No':<5}{'Make':<20}{'Model':<20}{'Year':<10}{'Roadtax Expiry':<15}{'VIN':<20}{'Price':<10}{'Status':<10}")
                print("=" * 80)
            else:
                print(f"{index:<5}{make:<20}{model:<20}{year:<10}{roadtax_expiry:<15}{vin:<20}{price:<10}{status:<10}")
    except Exception as e:
        print("Something went wrong when we listed the cars:", e)

def editCar(filename):
    try:
        with open(filename, "rt") as filehandler:
            lines = filehandler.readlines()
        data = [line.strip().split("|") for line in lines]

        print("=" * 80)
        print(f"{'No':<5}{'Make':<20}{'Model':<20}{'Year':<10}{'Roadtax Expiry':<15}{'VIN':<20}{'Price':<10}{'Status':<10}")
        print("=" * 80)
        for index, line in enumerate(data):
            if index == 0:
                continue
            make, model, year, roadtax_expiry, vin, price, status = line
            print(f"{index:<5}{make:<20}{model:<20}{year:<10}{roadtax_expiry:<15}{vin:<20}{price:<10}{status:<10}")

        index = keyboardInput(int, "Index of car to edit: ", "Index must be an integer")
        if index >= len(data) or index == 0:
            print("Sorry, not available :(")
        else:
            make, model, year, roadtax_expiry, vin, price, status = data[index]
            print(f"Make: {make}\nModel: {model}\nYear: {year}\nRoad Tax Expiry: {roadtax_expiry}\nVIN: {vin}\nPrice: {price}\nStatus: {status}")
            confirm = keyboardInput(str, "Are you sure? (y/n): ", "Incorrect response")
            if confirm.lower() == "y":
                newMake = keyboardInput(str, f"Make [{make}]: ", "Make must be a string") or make
                newModel = keyboardInput(str, f"Model [{model}]: ", "Model must be a string") or model
                newYear = keyboardInput(int, f"Year [{year}]: ", "Year must be an integer") or year
                newRoadtax = keyboardInput(str, f"Road Tax Expiry [{roadtax_expiry}]: ", "Road Tax Expiry must be a string") or roadtax_expiry
                newVin = keyboardInput(str, f"VIN [{vin}]: ", "VIN must be a string") or vin
                newPrice = keyboardInput(float, f"Price [{price}]: ", "Price must be a float") or price
                newStatus = keyboardInput(str, f"Status [{status}]: ", "Status must be a string") or status
                data[index] = [newMake, newModel, newYear, newRoadtax, newVin, newPrice, newStatus]

                with open(filename, "wt") as filehandler:
                    for line in data:
                        filehandler.write("|".join(map(str, line)) + "\n")
                print("Car edited successfully!")
    except Exception as e:
        print("Something went wrong when we edited the car:", e)

def removeCar(filename):
    try:
        with open(filename, "rt") as filehandler:
            lines = filehandler.readlines()
        data = [line.strip().split("|") for line in lines]

        print("=" * 80)
        print(f"{'No':<5}{'Make':<20}{'Model':<20}{'Year':<10}{'Roadtax Expiry':<15}{'VIN':<20}{'Price':<10}{'Status':<10}")
        print("=" * 80)
        for index, line in enumerate(data):
            if index == 0:
                continue
            make, model, year, roadtax_expiry, vin, price, status = line
            print(f"{index:<5}{make:<20}{model:<20}{year:<10}{roadtax_expiry:<15}{vin:<20}{price:<10}{status:<10}")

        index = keyboardInput(int, "Index of car to remove: ", "Index must be an integer")
        if index >= len(data) or index == 0:
            print("Sorry, not available :(")
        else:
            confirm = keyboardInput(str, "Are you sure? (y/n): ", "Incorrect response")
            if confirm.lower() == "y":
                data.pop(index)
                with open(filename, "wt") as filehandler:
                    for line in data:
                        filehandler.write("|".join(map(str, line)) + "\n")
                print("Car removed successfully!")
    except Exception as e:
        print("Something went wrong when we removed the car:", e)

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
            make, model, year, roadtax_expiry, vin, price, status = line
            roadtax_expiry_date = datetime.datetime.strptime(roadtax_expiry, "%Y-%m-%d").date()
            if roadtax_expiry_date < current_date:
                print(f"{index:<5}{make:<20}{model:<20}{year:<10}{roadtax_expiry:<15}{vin:<20}{price:<10}{status:<10}")
    except Exception as e:
        print("Something went wrong when checking pending road tax renewals:", e)



def updateCar(filename):
    try:
        with open(filename, "rt") as filehandler:
            lines = filehandler.readlines()
        data = [line.strip().split("|") for line in lines]

        print("=" * 80)
        print(f"{'No':<5}{'Make':<20}{'Model':<20}{'Year':<10}{'Roadtax Expiry':<15}{'VIN':<20}{'Price':<10}{'Status':<10}")
        print("=" * 80)
        for index, line in enumerate(data):
            if index == 0:
                continue
            make, model, year, roadtax_expiry, vin, price, status = line
            print(f"{index:<5}{make:<20}{model:<20}{year:<10}{roadtax_expiry:<15}{vin:<20}{price:<10}{status:<10}")

        index = keyboardInput(int, "Index of car to update price: ", "Index must be an integer")
        if index >= len(data) or index == 0:
            print("Sorry, not available :(")
        else:
            make, model, year, roadtax_expiry, vin, price, status = data[index]
            print(f"Make: {make}\nModel: {model}\nYear: {year}\nRoad Tax Expiry: {roadtax_expiry}\nVIN: {vin}\nPrice: {price}\nStatus: {status}")
            confirm = keyboardInput(str, "Are you sure? (y/n): ", "Incorrect response")
            if confirm.lower() == "y":
                newPrice = keyboardInput(float, f"New Price [{price}]: ", "Price must be a float") or price
                data[index] = [make, model, year, roadtax_expiry, vin, newPrice, status]

                with open(filename, "wt") as filehandler:
                    for line in data:
                        filehandler.write("|".join(map(str, line)) + "\n")
                print("Car price updated successfully!")
    except Exception as e:
        print("Something went wrong when we updated the car price:", e)

filename = "cars2.txt"
doMenu(filename)