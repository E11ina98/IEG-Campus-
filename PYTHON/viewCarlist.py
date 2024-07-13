################################
## Defining viewList function ##
################################
def viewList(filename):
    try:
        with open(filename,"r") as f:
            content = f.readlines()
            content = [i.strip().split(",") for i in content]
        
        print()
        print("=="*59)
        print(f"{"Make":12} {"Model":10} {"Year":7} {"Roadtax expiry date":25} {"Carplate":15} {"Cost price":15} {"Current price":18} {"Status"}")
        print("=="*59)
        
        for index,record in enumerate(content):
            make,model,year,roadtax_expiry_date,carplate,cost_price,current_car_price,status = record
            print(f"{index} {make:10} {model:10} {year:13} {roadtax_expiry_date:20} {carplate:7} {float(cost_price):17.2f} {float(current_car_price):16.2f} {status:>15}")
    except Exception as e:
        print(f"There problem in opening the file\n\n{e}")    