import datetime

class CarManagementSystem:
    def __init__(self, filename):
        self.filename = filename

    def keyboardInput(self, datatype, caption, errorMessage, defaultValue=None):
        value = None
        isInvalid = True
        while isInvalid:
            try:
                if defaultValue is None:
                    value = datatype(input(caption))
                else:
                    value = input(caption)
                    if value.strip() == "":
                        value = defaultValue
                    else:
                        value = datatype(value)
            except Exception as e:
                print(errorMessage, "\n", e)
            else:
                isInvalid = False
        return value

    def viewList(self):
        try:
            with open(self.filename, "r") as f:
                content = f.readlines()
                content = [i.strip().split("|") for i in content]
        
            print()
            print("=" * 129)
            print(f"{' ':<3}{'Make':<13} {'Model':<10} {'Year':^10} {'Roadtax expiry date':<20} {'Carplate':>15} {'Cost price':>15} {'Current price':>20} {'Status':^20}")
            print("=" * 129)
        
            for index, record in enumerate(content):
                make, model, year, roadtax_expiry_date, carplate, cost_price, current_car_price, status = record
                roadtax_expiry_date = roadtax_expiry_date.replace(".", "/")
                reformatted_roadtax_expiry_date = datetime.datetime.strptime(roadtax_expiry_date, "%d/%m/%Y")
                reformatted_roadtax_expiry_date = reformatted_roadtax_expiry_date.strftime("%d/%m/%Y")
                print(f"{index:<3}{make:<13} {model:<10} {year:^10} {str(reformatted_roadtax_expiry_date):^20} {carplate:>15} {float(cost_price):>15.2f} {float(current_car_price):>20.2f} {status:^20}")
        except Exception as e:
            print(f"There was a problem in opening the file\n\n{e}")

    def addCar(self):
        try:
            with open(self.filename, "r+") as f:
                content = f.readlines()
                content = [i.strip().split("|") for i in content]
            
                make = self.keyboardInput(str, "Enter the car make: ", "The car make must be a string.")
                model = self.keyboardInput(str, "Enter the car model: ", "The car model must be a string.")
                year = self.keyboardInput(int, "Enter the car year: ", "The year must be an integer.")
                roadtax_expiry_date = self.keyboardInput(str, "Enter the car roadtax expiry date: ", "The date format is dd/mm/yyyy.")
                carplate = self.keyboardInput(str, "Enter the carplate: ", "The input is invalid.")
                cost_price = self.keyboardInput(float, "Enter the car cost price: ", "The input is invalid.")
                current_car_price = self.keyboardInput(float, "Enter the current car price: ", "The input is invalid.")
                status = self.keyboardInput(str, "Enter the car status: ", "The input is invalid.")
                
                new_car = [make, model, year, roadtax_expiry_date, carplate, cost_price, current_car_price, status]
                content.append(new_car)
                updated_content = []
                for i in range(len(content)):
                    line = "|".join([str(j) for j in content[i]]) + ("\n" if i != (len(content) - 1) else "")
                    updated_content.append(line)
                
            with open(self.filename, "w") as f:
                f.writelines(updated_content)
        except Exception as e:
            print(f"Problem in reading the file\n\n{e}")

    def editCar(self):
        try:
            with open(self.filename, "r") as f:
                content = f.readlines()
                content = [i.strip().split("|") for i in content]

            self.viewList()
            
            index = self.keyboardInput(int, "\nIndex of car to edit: ", "Index must be an integer")
            if index >= len(content):
                print("Sorry, not available :(")
            else:
                make, model, year, roadtax_expiry_date, carplate, cost_price, current_car_price, status = content[index]
             
                print(f"Make: {make}\nModel: {model}\nYear: {year}\nRoad Tax Expiry: {roadtax_expiry_date}\nCarplate: {carplate}\nCost Price: {float(cost_price):.2f}\nCurrent Price: {float(current_car_price):.2f}\nStatus: {status}")
                confirm = self.keyboardInput(str, "Are you sure? (y/n): ", "Incorrect response")
                if confirm.lower() == "y":
                    newMake = self.keyboardInput(str, f"Make [{make}]: ", "Make must be a string", make)
                    newModel = self.keyboardInput(str, f"Model [{model}]: ", "Model must be a string", model)
                    newYear = self.keyboardInput(int, f"Year [{year}]: ", "Year must be an integer", year)
                    newRoadtax = self.keyboardInput(str, f"Road Tax Expiry [{roadtax_expiry_date}]: ", "Road Tax Expiry must be a string", roadtax_expiry_date)
                    newCarplate = self.keyboardInput(str, f"Car Plate [{carplate}]: ", "Car plate must be a string", carplate)
                    newCostprice = self.keyboardInput(float, f"Cost Price [{float(cost_price):.2f}]: ", "Cost Price must be a float", cost_price)
                    newCurrentprice = self.keyboardInput(float, f"Current Price [{float(current_car_price):.2f}]: ", "Current Price must be a float", current_car_price)
                    newStatus = self.keyboardInput(str, f"Status [{status}]: ", "Status must be a string", status)
                    content[index] = [newMake, newModel, newYear, newRoadtax, newCarplate, newCostprice, newCurrentprice, newStatus]

                    with open(self.filename, "w") as filehandler:
                        for line in content:
                            filehandler.write("|".join(map(str, line)) + "\n")
                    print("Car edited successfully!")
        except Exception as e:
            print("Something went wrong when we edited the car:", e)

    def removeCar(self):
        try:
            with open(self.filename, "r") as f:
                content = f.readlines()
                content = [i.strip() for i in content]
            choice = None
            while choice != 0:
                print()
                print("=======================")
                print("||   0. Exit         ||")
                print("||   1. Remove car   ||")
                print("=======================")
                choice = self.keyboardInput(int, "\nPlease select your choice\n", "Inputted choice must be an integer.")
                if choice == 1:
                    self.viewList()
                    index = self.keyboardInput(int, "Enter the index of the car to be removed: ", "The index must be an integer.")
                    confirmation = self.keyboardInput(str, "Do you confirm to remove this car?(y/n): ", "Invalid input.")
                    if confirmation.lower() == "y":
                        del content[index]
                        with open(self.filename, "w") as f:
                            updated_content = [line + "\n" if i != (len(content) - 1) else line for i, line in enumerate(content)]
                            f.writelines(updated_content)
                        print("Car removed.")
                else:
                    print("The option selected is not valid.")
        except Exception as e:
            print(f"Problem in reading the file.\n\n{e}")

    def pendingRoadtaxRenewal(self):
        try:
            current_date = datetime.datetime.today().date()
            with open(self.filename, "r") as f:
                content = f.readlines()
                content = [i.strip().split("|") for i in content]
            
            print("\nPending road tax renewals:\n")
            
            for index, record in enumerate(content):
                make, model, year, roadtax_expiry_date, carplate, cost_price, current_car_price, status = record
                roadtax_expiry_date = datetime.datetime.strptime(roadtax_expiry_date, "%d.%m.%Y").date()
                if roadtax_expiry_date < current_date:
                    print(f"{index:<5}{make:<15}{model:<15}{year:<15}{str(roadtax_expiry_date):<20}{carplate:<15}{float(cost_price):<15.2f}{float(current_car_price):<15.2f}{status}")
            
            choice = self.keyboardInput(str, "\nDo you want to update the roadtax expiry date?(y/n): ", "Invalid choice.")
            
            if choice.lower() == "y":
                index_to_update = self.keyboardInput(int, "\nPlease enter the index of roadtax date to be updated: ", "Index entered is invalid.")
                new_date = self.keyboardInput(str, "Please enter the new roadtax expiry date: ", "The date entered is invalid.")
                content[index_to_update][3] = new_date
                with open(self.filename, "w") as f:
                    updated_content = ["|".join(line) + "\n" if i != (len(content) - 1) else "|".join(line) for i, line in enumerate(content)]
                    f.writelines(updated_content)
                print("Updated successfully.")
        except Exception as e:
            print(f"Problem in updating the roadtax expiry date\n\n{e}")

    def updateCarprice(self):
        try:
            with open(self.filename, "r") as f:
                content = f.readlines()
                content = [i.strip().split("|") for i in content]
            
            self.viewList()
            index_to_update = self.keyboardInput(int, "\nPlease enter the index of the car: ", "The index must be an integer.")
            
            current_price = content[index_to_update][6]
            print(f"Current car price is {current_price}")
            choice = None
            while choice != 0:
                updated_price = self.keyboardInput(float, "Enter the new car price: ", "The price entered is invalid.")
                confirm = self.keyboardInput(str, f"Confirm to update the price to {updated_price}?(y/n): ", "Invalid choice.")
                if confirm.lower() == "y":
                    content[index_to_update][6] = updated_price
                    new_content = ["|".join(map(str, line)) + "\n" if i != (len(content) - 1) else "|".join(map(str, line)) for i, line in enumerate(content)]
                    with open(self.filename, "w") as f:
                        f.writelines(new_content)
                    
                    print("============================================")
                    print("||   0. Exit                              ||")
                    print("||   1. Continue to update current price  ||")
                    print("============================================")
                    choice = self.keyboardInput(int, "Please select your option:\n", "Invalid input.")
        except Exception as e:
            print(f"Problem in updating the car price.\n\n{e}")

    def menu(self):
        choice = None
        while choice != 0:
            print()
            print("=======================================")
            print("||   0. Exit                         ||")
            print("||   1. View car list                ||")
            print("||   2. Add car                      ||")
            print("||   3. Edit car                     ||")
            print("||   4. Remove car                   ||")
            print("||   5. Renew roadtax expiry date    ||")
            print("||   6. Update current car price     ||")
            print("=======================================")
            choice = self.keyboardInput(int, "Please select the option: ", "The selection made is invalid.")
            if choice == 1:
                self.viewList()
            elif choice == 2:
                self.addCar()
            elif choice == 3:
                self.editCar()
            elif choice == 4:
                self.removeCar()
            elif choice == 5:
                self.pendingRoadtaxRenewal()
            elif choice == 6:
                self.updateCarprice()
            else:
                choice = 0

# Testing the program
cms = CarManagementSystem("car_3.txt")
cms.menu()
