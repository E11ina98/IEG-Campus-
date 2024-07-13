import json

try:
    with open('KedaiElektronik2.json', 'r') as filehandler:
        data = json.load(filehandler)
        print(type(data))
        
        for product in data:
            print(product)

except Exception as e:
    print("Something went wrong:", e)