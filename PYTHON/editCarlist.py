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