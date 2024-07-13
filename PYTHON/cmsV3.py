import datetime

class CarManagementSystem:
    def __init__(self, filename):
        self.filename = filename

#################################
## Defining the keyboard input ##
#################################
    def keyboardInput(self,datatype,caption, errorMessage, defaultValue= None):
        value= None
        isInvalid = True
        while isInvalid == True:
            try:
                if defaultValue == None:
                    value= datatype(input(caption))
                else:
                    value= input(caption)
                    if (value.strip() == ""):
                        value = defaultValue
                    else:
                        value= datatype(value)
            except Exception as e:
                print(errorMessage,"\n",e)
            else:
                isInvalid = False
        return value
        
################################
## Defining viewList function ##
################################
    def viewList(self):
        try:
            with open(self.filename,"r") as f:
                content = f.readlines()
                content = [i.strip().split("|") for i in content]
        
            print()
            print("="*125)
            print(f"{" ":<3}{"Make":<13} {"Model":<10} {"Year":^10} {"Roadtax expiry date":<20} {"Carplate":>15} {"Cost price":>15} {"Current price":>20} {"Status":^15}")
            print("="*125)
        
            for index,record in enumerate(content):
                make,model,year,roadtax_expiry_date,carplate,cost_price,current_car_price,status = record
                print(f"{index:<3}{make:<13} {model:<10} {year:^10} {roadtax_expiry_date:^20} {carplate:>15} {float(cost_price):>15.2f} {float(current_car_price):>20.2f} {status:^15}")
        except Exception as e:
            print(f"There problem in opening the file\n\n{e}")    
    
    
# ## Testing the function
# filename = "car.txt"
# viewList(filename)

##############################
## Defining addCar function ##
##############################
    def addCar(self):
        try:    
            with open(self.filename,"r+") as f:
            # reading the file and storing it into variable
                content = f.readlines()
                content = [i.strip().split(",") for i in content]
            
            # prompting user for new car information
                make = self.keyboardInput(str,"Enter the car make: ","The care make must be a string.")
                model = self.keyboardInput(str,"Enter the car model: ","The car model must be a string.")
                year = self.keyboardInput(int,"Enter the car year: ","The year must be integer.")
                roadtax_expiry_date = self.keyboardInput(str,"Enter the car roadtax expiry date: ","The date format is dd/mm/yyyy.")
                carplate = self.keyboardInput(str,"Enter the carplate: ","The input invalid.")
                cost_price = self.keyboardInput(float,"Enter the car cost price: ","The input invalid.")
                current_car_price = self.keyboardInput(float,"Enter the current car price: ","The input invalid.")
                status = self.keyboardInput(str,"Enter the car status: ","The input invalid.")
            # updating the content
                new_car = [make,model,year,roadtax_expiry_date,carplate,cost_price,current_car_price,status]
                content.append(new_car)
                updated_content = []
                for i in range(len(content)):
                    if i != (len(content)-1):
                        line = "|".join([str(j) for j in content[i]]) + "\n"
                        updated_content.append(line)
                    else:
                        line = "|".join([str(j) for j in content[i]])
                        updated_content.append(line)
        # writing the updated content into the txt
            with open(self.filename,"w+") as f:
                f.writelines(updated_content)
        except Exception as e:
            print(f"Problem in reading the file\n\n{e}")

# ## testing the addCar function
# filename = "car.txt"
# addCar(filename)

#################################
## Defining editCar function ##
#################################
    def editCar(self):
        try:
            with open(self.filename,"r") as f:
                content = f.readlines()
                content = [i.strip().split("|") for i in content]

            print()
            print("=="*59)
            print(f"{"Make":12} {"Model":10} {"Year":7} {"Roadtax expiry date":25} {"Carplate":15} {"Cost price":15} {"Current price":18} {"Status"}")
            print("=="*59)

            for index, record in enumerate(content):
                if index == 0:
                    continue
                make,model,year,roadtax_expiry_date,carplate,cost_price,current_car_price,status = record
                print(f"{index:<5}{make:<20}{model:<20}{year:<10}{roadtax_expiry_date:<15}{carplate:<20}{cost_price:<15}{current_car_price:<15}{status:<10}")

            index = self.keyboardInput(int, "Index of car to edit: ", "Index must be an integer")
            if index >= len(content) or index == 0:
                print("Sorry, not available :(")
            else:
                make, model, year, roadtax_expiry_date, carplate, cost_price, current_car_price, status = content[index]
                print(f"Make: {make}\nModel: {model}\nYear: {year}\nRoad Tax Expiry: {roadtax_expiry_date}\nCarplate: {carplate}\nCost Price: {cost_price}\nCurrent Price: {current_car_price}\nStatus: {status}")
                confirm = self.keyboardInput(str, "Are you sure? (y/n): ", "Incorrect response")
                if confirm.lower() == "y":
                    newMake = self.keyboardInput(str, f"Make [{make}]: ", "Make must be a string") or make
                    newModel = self.keyboardInput(str, f"Model [{model}]: ", "Model must be a string") or model
                    newYear = self.keyboardInput(int, f"Year [{year}]: ", "Year must be an integer") or year
                    newRoadtax = self.keyboardInput(str, f"Road Tax Expiry [{roadtax_expiry_date}]: ", "Road Tax Expiry must be a string") or roadtax_expiry_date
                    newCarplate = self.keyboardInput(str, f"Car Plate [{carplate}]: ", "Car plate must be a string") or carplate
                    newCostprice = self.keyboardInput(float, f"Cost Price [{cost_price}]: ", "Cost Price must be a float") or cost_price
                    newCurrentprice = self.keyboardInput(float, f"Current Price [{current_car_price}]: ", "Current Price must be a float") or current_car_price
                    newStatus = self.keyboardInput(str, f"Status [{status}]: ", "Status must be a string") or status
                    content[index] = [newMake, newModel, newYear, newRoadtax, newCarplate, newCostprice, newCurrentprice, newStatus]

                    with open(self.filename, "wt") as filehandler:
                        for line in content:
                            filehandler.write("|".join(map(str, line)) + "\n")
                    print("Car edited successfully!")
        except Exception as e:
            print("Something went wrong when we edited the car:", e)


#################################
## Defining removeCar function ##
#################################
    def removeCar(self):
        try:
            with open(self.filename,"r+") as f:
                content = f.readlines()
                content_stripped = [i.strip() for i in content]
            choice=None
            while choice != 0:
                print()
                print("=======================")
                print("||   0. Exit         ||")
                print("||   1. Remove car   ||")
                print("=======================")
                choice = self.keyboardInput(int,"\nPlease select your choice\n","Inputted choice must be integer.")
                if choice == 1:
                    self.viewList()
                    index = self.keyboardInput(int,"Enter the index of car to be removed: ","The index must be an integer.")
                    confirmation = self.keyboardInput(str,"Do you confirm to remove this car?(y/n)","Invalid input.")
                    if confirmation == "y":
                        del content_stripped[index]
                        with open(self.filename,"w+") as f:
                            updated_content = []
                            for i in range(len(content_stripped)):
                                if i != (len(content_stripped)-1): 
                                    updated_content.append(content_stripped[i]+"\n")
                                else:
                                    updated_content.append(content_stripped[i])
                            f.writelines(updated_content)
                        print("Car removed.")
                        # choice = keyboardInput(int,"\nPlease select your choice . .\n","Inputted choice must be integer.")
                else:
                    choice = 0
        except Exception as e:
            (print(f"Problem in reading the file.\n\n{e}"))

# ## testing the function
# filename = "car.txt"
# removeCar(filename)

############################################
## Defining pendingRoadTaxRenewal function ##
############################################

    def pendingRoadtaxRenewal(self):
        try:
            current_date = datetime.datetime.today().date()
            with open(self.filename, "rt") as f:
                content = f.readlines()
                content = [i.strip().split("|") for i in content]
            
            print()
            print("Pending road tax renewals:")
            
            for index, record in enumerate(content):
                if index == 0:
                    continue
                make,model,year,roadtax_expiry_date,carplate,cost_price,current_car_price,status = record
                roadtax_expiry_date = datetime.datetime.strptime(roadtax_expiry_date, "%d.%m.%Y").date()
                if roadtax_expiry_date < current_date:
                    print(f"{index:<5}{make:<15}{model:<15}{year:<15}{str(roadtax_expiry_date):<20}{carplate:<15}{float(cost_price):<15.2f}{float(current_car_price):<15.2f}{status}")   
        except Exception as e:
            print("Something went wrong when checking pending road tax renewals:", e)


######################################
## Defining updateCarprice function ##
######################################
    def specific_listing(self):
        try:
            with open(self.filename, "r") as f:
                    content = f.readlines()
                    content_stripped = [i.strip() for i in content]
                    content_stripped_splitted = [i.split("|") for i in content_stripped]
            print("=="*51)
            print(f"{"Index":10} {"Make":20} {"Model":15} {"Year":15} {"Cost Price":20} {"Current Car Price":20}")
            print("=="*51)
            for index,record in enumerate(content_stripped_splitted):
                make,model,year,roadtax_expiry_date,carplate,cost_price,current_car_price,status = record
                print(f"{index:<10} {make:<20} {model:<15} {year:15} {float(cost_price):>10.2f} {float(current_car_price):>25.2f}")
        except Exception as e:
            print(f"Problem in reading the file\n\n{e}")

    def updateCarprice(self):
        choice = 1
        try:
            while choice == 1:      
                # reading the file
                with open(self.filename,"r+") as f:
                    content = f.readlines()
                    content_stripped_splitted = [i.strip().split("|") for i in content]
                    # showing focused listing and getting the index with current price
                    print()
                    self.specific_listing()
                    selected_index = self.keyboardInput(int,"Please enter the car index:\n","Error: Index must be integer.")
                    current_price = self.keyboardInput(float,"Please enter the current car price:\n","The input must be a valid number.")
                    
                # updating content and writing to the file
                    content_stripped_splitted[selected_index][6] = current_price
                with open(self.filename,"w+") as f:
                    new_content = []
                    for i in range(len(content_stripped_splitted)):
                        if i == (len(content_stripped_splitted)-1):
                            line = [str(j) for j in content_stripped_splitted[i]]
                            line = "|".join(line)
                            new_content.append(line)
                        else:
                            line = [str(j) for j in content_stripped_splitted[i]]
                            line = "|".join(line) + "\n"
                            new_content.append(line)
                    f.writelines(new_content)
                    
                print("============================================")
                print("||   0. Exit                              ||")
                print("||   1. Continue to update current price  ||")
                print("============================================")
                choice = self.keyboardInput(int,"Please select your option:\n","Invalid input.")
        except Exception as e:
            print(f"Problem in reading the file\n\n{e}")

# ## testing the function
# filename = "care.txt"
# updateCarprice(filename)

############################
## Defining menu function ##
############################
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
            choice = self.keyboardInput(int,"Please select the option: ","The selection made is invalid.")
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


################################################################################################
################################################################################################
## Testing the program ##
if __name__ == "__main__":
    filename = "car.txt"
    cms = CarManagementSystem(filename)
    cms.menu()
#menu(filename)
#viewList(filename)
#editCar(filename)
#pendingRoadtaxRenewal(filename)