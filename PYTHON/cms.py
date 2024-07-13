import datetime
import os

class Car:
    def __init__(self, make, model, year, vin, price, status, road_tax_expiry):
        self.make = make
        self.model = model
        self.year = year
        self.vin = vin
        self.price = price
        self.status = status
        self.road_tax_expiry = datetime.datetime.strptime(road_tax_expiry, '%Y-%m-%d')

    def __str__(self):
        return f"{self.year} {self.make} {self.model} (VIN: {self.vin}, Price: {self.price}, Status: {self.status}, Road Tax Expiry: {self.road_tax_expiry.strftime('%Y-%m-%d')})"

    def to_dict(self):
        return {
            'make': self.make,
            'model': self.model,
            'year': self.year,
            'vin': self.vin,
            'price': self.price,
            'status': self.status,
            'road_tax_expiry': self.road_tax_expiry.strftime('%Y-%m-%d')
        }

    @staticmethod
    def from_dict(car_dict):
        return Car(
            car_dict['make'],
            car_dict['model'],
            car_dict['year'],
            car_dict['vin'],
            car_dict['price'],
            car_dict['status'],
            car_dict['road_tax_expiry']
        )


class CarManager:
    def __init__(self, filename='cars.txt'):
        self.filename = filename
        self.cars = self.load_cars()

    def load_cars(self):
        cars = []
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                for line in file:
                    car_dict = eval(line.strip())
                    cars.append(Car.from_dict(car_dict))
        return cars

    def save_cars(self):
        with open(self.filename, 'w') as file:
            for car in self.cars:
                file.write(f"{car.to_dict()}\n")

    def list_cars(self):
        return self.cars

    def add_car(self, car):
        self.cars.append(car)
        self.save_cars()

    def edit_car(self, vin, make=None, model=None, year=None, price=None, status=None, road_tax_expiry=None):
        car = self.find_car_by_vin(vin)
        if car:
            if make:
                car.make = make
            if model:
                car.model = model
            if year:
                car.year = year
            if price:
                car.price = price
            if status:
                car.status = status
            if road_tax_expiry:
                car.road_tax_expiry = datetime.datetime.strptime(road_tax_expiry, '%Y-%m-%d')
            self.save_cars()
            return car
        return None

    def remove_car(self, vin):
        self.cars = [car for car in self.cars if car.vin != vin]
        self.save_cars()

    def find_car_by_vin(self, vin):
        for car in self.cars:
            if car.vin == vin:
                return car
        return None

    def pending_road_tax_renewal(self):
        current_date = datetime.datetime.today()
        return [car for car in self.cars if car.road_tax_expiry < current_date]

    def update_car_price(self, vin, new_price):
        car = self.find_car_by_vin(vin)
        if car:
            car.price = new_price
            self.save_cars()
            return car
        return None


def main():
    car_manager = CarManager()

    while True:
        print("\nCar Management System")
        print("1. List all cars")
        print("2. Add a new car")
        print("3. Edit an existing car")
        print("4. Remove a car")
        print("5. Check pending road tax renewals")
        print("6. Update car price")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nListing all cars:")
            for car in car_manager.list_cars():
                print(car)

        elif choice == '2':
            make = input("Enter car make: ")
            model = input("Enter car model: ")
            year = int(input("Enter car year: "))
            vin = input("Enter car VIN: ")
            price = float(input("Enter car price: "))
            status = input("Enter car status: ")
            road_tax_expiry = input("Enter road tax expiry date (YYYY-MM-DD): ")
            car = Car(make, model, year, vin, price, status, road_tax_expiry)
            car_manager.add_car(car)
            print("Car added successfully!")

        elif choice == '3':
            vin = input("Enter VIN of the car to edit: ")
            make = input("Enter new make (leave blank to keep current): ")
            model = input("Enter new model (leave blank to keep current): ")
            year = input("Enter new year (leave blank to keep current): ")
            price = input("Enter new price (leave blank to keep current): ")
            status = input("Enter new status (leave blank to keep current): ")
            road_tax_expiry = input("Enter new road tax expiry date (YYYY-MM-DD, leave blank to keep current): ")
            car_manager.edit_car(vin, make if make else None, model if model else None, int(year) if year else None, float(price) if price else None, status if status else None, road_tax_expiry if road_tax_expiry else None)
            print("Car edited successfully!")

        elif choice == '4':
            vin = input("Enter VIN of the car to remove: ")
            car_manager.remove_car(vin)
            print("Car removed successfully!")

        elif choice == '5':
            print("\nListing cars pending road tax renewal:")
            for car in car_manager.pending_road_tax_renewal():
                print(car)

        elif choice == '6':
            vin = input("Enter VIN of the car to update price: ")
            new_price = float(input("Enter new price: "))
            car_manager.update_car_price(vin, new_price)
            print("Car price updated successfully!")

        elif choice == '7':
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

