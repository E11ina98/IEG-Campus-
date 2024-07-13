from os.path import exists
from datetime import datetime

# Function to read booking data from file
def read_booking_data(file_name):
    bookings = []
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines[1:]:  # Skip the header line
            if line.strip():  # Check if line is not empty
                booking = line.strip().split('|')
                bookings.append({
                    'Car': booking[0].strip(),
                    'Driver': booking[1].strip(),
                    'Customer': booking[2].strip(),
                    'Start date': booking[3].strip(),
                    'End date': booking[4].strip(),
                    'Rating Status': booking[5].strip()
                })
    return bookings

# Function to write booking data back to file
def write_booking_data(file_name, bookings):
    with open(file_name, 'w') as file:
        file.write("Car | Driver | Customer | Start date | End date | Rating Status\n")
        for booking in bookings:
            file.write(f"{booking['Car']} | {booking['Driver']} | {booking['Customer']} | {booking['Start date']} | {booking['End date']} | {booking['Rating Status']}\n")

# Function to check if rating can be given based on rating status
def can_rate_booking(booking):
    if booking['Rating Status'] == 'No':
        return True
    return False

# Function to update rating status after rating given
def update_rating_status(booking):
    booking['Rating Status'] = 'Yes'

# Function to handle user input and validation
def get_user_input(prompt, data_type=str):
    while True:
        try:
            user_input = data_type(input(prompt).strip())
            return user_input
        except ValueError:
            print("Invalid input. Please try again.")

# Function to handle rating process
def rate_driver(booking):
    professionalism = get_user_input("Professionalism (1-5): ", int)
    punctuality = get_user_input("Punctuality (1-5): ", int)
    behavior = get_user_input("Behavior (1-5): ", int)
    average_rating = (professionalism + punctuality + behavior) / 3.0
    print(f"Average rating for driver {booking['Driver']}: {average_rating:.2f}")
    update_driver_rating(booking['Driver'], professionalism, punctuality, behavior, average_rating)
    booking['driver_rated'] = True  # Mark as driver rated

def rate_car(booking):
    comfort = get_user_input("Comfort (1-5): ", int)
    cleanliness = get_user_input("Cleanliness (1-5): ", int)
    average_rating = (comfort + cleanliness) / 2.0
    print(f"Average rating for car {booking['Car']}: {average_rating:.2f}")
    update_car_rating(booking['Car'], comfort, cleanliness, average_rating)
    booking['car_rated'] = True  # Mark as car rated

# Function to list ratings for the driver or car from rating.txt
def list_ratings(booking):
    print(f"\nListing ratings for driver {booking['Driver']} and car {booking['Car']}:")
    try:
        with open("rating.txt", 'r') as file:
            lines = file.readlines()
            for line in lines:
                if booking['Driver'] in line or booking['Car'] in line:
                    print(line.strip())
    except Exception as e:
        print("Something went wrong when listing the ratings:", e)

# Function to update driver rating in rating.txt
def update_driver_rating(driver, professionalism, punctuality, behavior, rating):
    with open("rating.txt", 'a') as file:
        file.write(f"Driver: {driver} | Professionalism Rating: {professionalism:.2f} | Punctuality Rating: {punctuality:.2f} | Behavior rating: {behavior:.2f} | Average Rating: {rating:.2f}\n")

# Function to update car rating in rating.txt
def update_car_rating(car, comfort, cleanliness, rating):
    with open("rating.txt", 'a') as file:
        file.write(f"Car: {car} | Comfort Rating: {comfort:.2f} | Cleanliness Rating: {cleanliness:.2f} | Average Rating: {rating:.2f}\n")

# Function to print booking data in a formatted table
def printBookingData(filename):
    try:
        if not exists(filename):
            print(f"The file '{filename}' does not exist.")
            return
        
        lines = None
        with open(filename, "rt") as filehandler:
            lines = filehandler.readlines()
        
        print("=" * 30 + " BOOKING DATA " + "=" * 30)
        print("{:<5}{:<10}{:<15}{:<15}{:<12}{:<12}{:<15}".format(
            "No.", "Car", "Driver", "Customer", "Start date", "End date", "Rating Status"))
        print("=" * 85)
        
        for index, line in enumerate(lines):
            if index == 0:
                continue  # Skip header line
            car, driver, customer, start_date, end_date, rating_status = line.strip().split("|")
            print(f"{index:<5}{car.strip():<10}{driver.strip():<15}{customer.strip():<15}{start_date.strip():<12}{end_date.strip():<12}{rating_status.strip():<15}")

        print("=" * 85)
    except Exception as e:
        print("Something went wrong when printing booking data:", e)

# Function to generate an analytic report
def generate_analytic_report():
    try:
        driver_ratings = {}
        car_ratings = {}
        driver_trips = {}
        car_trips = {}
        
        with open("rating.txt", 'r') as file:
            lines = file.readlines()
            for line in lines:
                if "Driver" in line:
                    parts = line.strip().split("|")
                    driver = parts[0].split(":")[1].strip()
                    professionalism = float(parts[1].split(":")[1].strip())
                    punctuality = float(parts[2].split(":")[1].strip())
                    behavior = float(parts[3].split(":")[1].strip())
                    average = float(parts[4].split(":")[1].strip())
                    if driver in driver_ratings:
                        driver_ratings[driver]["Professionalism"].append(professionalism)
                        driver_ratings[driver]["Punctuality"].append(punctuality)
                        driver_ratings[driver]["Behavior"].append(behavior)
                        driver_ratings[driver]["Overall"].append(average)
                        driver_trips[driver] += 1
                    else:
                        driver_ratings[driver] = {
                            "Professionalism": [professionalism],  
                            "Punctuality": [punctuality],  
                            "Behavior": [behavior],  
                            "Overall": [average]   
                        }
                        driver_trips[driver] = 1
                elif "Car" in line:
                    parts = line.strip().split("|")
                    car = parts[0].split(":")[1].strip()
                    comfort = float(parts[1].split(":")[1].strip())
                    cleanliness = float(parts[2].split(":")[1].strip())
                    average = float(parts[3].split(":")[1].strip())
                    if car in car_ratings:
                        car_ratings[car]["Comfort"].append(comfort)
                        car_ratings[car]["Cleanliness"].append(cleanliness)
                        car_ratings[car]["Overall"].append(average)
                        car_trips[car] += 1
                    else:
                        car_ratings[car] = {
                            "Comfort": [comfort],  
                            "Cleanliness": [cleanliness],  
                            "Overall": [average]
                        }
                        car_trips[car] = 1

        print("\nAnalytic Report")
        print("=" * 50)
        print("Driver Ratings:")
        for driver, ratings in driver_ratings.items():
            print(f"\n{driver}: Trips = {driver_trips[driver]}")
            for category, values in ratings.items():
                avg_rating = sum(values) / len(values)
                print(f"Average {category} Rating = {avg_rating:.2f}")

        print("\nCar Ratings:")
        for car, ratings in car_ratings.items():
            print(f"\n{car}: Trips = {car_trips[car]}")
            for category, values in ratings.items():
                avg_rating = sum(values) / len(values)
                print(f"Average {category} Rating = {avg_rating:.2f}")
        print("=" * 50)
    except Exception as e:
        print("Something went wrong when generating the analytic report:", e)

# Function to handle the rating journey process
def rate_journey(booking):
    driver_rated = False
    car_rated = False
    while True:
        print(f"\nRate your journey for Driver: {booking['Driver']} and Car: {booking['Car']}:")
        print("==========================")
        print("| 0 - Back to Main Menu |")
        print("| 1 - Rate the driver   |")
        print("| 2 - Rate the car      |")
        print("| 3 - List Ratings      |")
        print("==========================")
        choice = get_user_input("Enter choice (0-3): ", int)

        if choice == 0:
            if not driver_rated or not car_rated:
                if not driver_rated:
                    print("No rating was submitted for the driver.")
                if not car_rated:
                    print("No rating was submitted for the car.")
            return driver_rated and car_rated  # Return True if both ratings were made, otherwise False
        elif choice == 1:
            if driver_rated:
                print("Driver has already been rated. Do you want to edit the rating?")
                if get_user_input("Edit rating? (yes/no): ", str).lower() != 'yes':
                    continue
            rate_driver(booking)
            driver_rated = True
        elif choice == 2:
            if car_rated:
                print("Car has already been rated. Do you want to edit the rating?")
                if get_user_input("Edit rating? (yes/no): ", str).lower() != 'yes':
                    continue
            rate_car(booking)
            car_rated = True
        elif choice == 3:
            list_ratings(booking)
        else:
            print("Invalid choice. Please enter a number from 0 to 3.")

        if driver_rated and car_rated:
            print("\nBoth driver and car have been rated.")
            print("\nThank you for your rating!")
        else:
            if not driver_rated:
                print("\nDriver has not been rated yet.")
            if not car_rated:
                print("\nCar has not been rated yet.")

# Function to run the rating system
def run_rating_system():
    booking_file = "booking.txt"
    bookings = read_booking_data(booking_file)

    while True:
        print("\nMain Menu:")
        print("==================")
        print("| 0 - Exit       |")
        print("| 1 - List       |")
        print("| 2 - Add Rating |")
        print("| 3 - Analytics  |")
        print("==================")
        choice = get_user_input("Choice [0,1,2,3]: ", int)

        if choice == 0:
            print("Thank you for using the rating system.")
            break
        elif choice == 1:
            printBookingData(booking_file)
        elif choice == 2:
            print("\nBookings available for rating:")
            rateable_bookings = [(i + 1, booking) for i, booking in enumerate(bookings) if can_rate_booking(booking)]
            if not rateable_bookings:
                print("No bookings available for rating.")
                continue
            for index, booking in rateable_bookings:
                print(f"{index}. Car: {booking['Car']} | Driver: {booking['Driver']} | Customer: {booking['Customer']} | Start date: {booking['Start date']} | End date: {booking['End date']}")

            index_to_rate = int(input("\nEnter the index of the booking you want to rate (1, 2, ...): "))
            booking_to_rate = next((booking for idx, booking in rateable_bookings if idx == index_to_rate), None)

            if booking_to_rate:
                rating_made = rate_journey(booking_to_rate)
                if rating_made:
                    update_rating_status(booking_to_rate)
                    write_booking_data(booking_file, bookings)
                    print("\nThank you for your rating!")
                else:
                    print("\nNo rating was submitted. Returning to Main Menu.")
            else:
                print("Invalid selection. Please choose a valid index.")
        elif choice == 3:
            generate_analytic_report()
        else:
            print("Invalid choice. Please enter a number from 0 to 3.")

# Run the rating system
run_rating_system()



# Run the rating system
run_rating_system()
