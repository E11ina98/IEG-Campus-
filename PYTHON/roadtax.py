import datetime

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