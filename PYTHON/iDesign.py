#QUESTION 1

#First line of the input is a string that corresponds to a Customer’s name. Assume that the maximum length of the string is 50.
#Output should display the welcome message along with the Customer’s name

name= "Beena"
inputstring= "Hello " + name + "! Welcome to Amphi Event Management System" 
print (inputstring)

#QUESTION 2

#Estimate the total expenses incurred by an event and the percentage rate of each of the expenses involved in planning and executing an event
# Variable
# branding expenses, travel expenses, food expenses and logistics expenses as input from the user 
# Calculate
# the total expenses for an event and the percentage rate of each of these expenses

branding = float(input("Enter branding expenses " ))
travel= float(input("Enter travel expenses "))
food= float(input("Enter food expenses " ))
logistic = float(input("Enter logistics expenses "))

total= (branding + travel + food + logistic)
print(f"Total expenses : Rs.{total:.2f}")

branding_percentage= branding / total* 100
travel_percentage= travel / total* 100
food_percentage= food / total* 100
logistic_percentage= logistic / total* 100

print(f"Branding expenses percentage : {branding_percentage:.2f}%")
print(f"Travel expenses percentage : {travel_percentage:.2f}%")
print(f"Food expenses percentage : {food_percentage:.2f}%")
print(f"Logistics expenses percentage : {logistic_percentage:.2f}%")

# Question 3
#sold 'X' more adult tickets than children tickets and
#sold twice as many senior tickets as children tickets
# adult ticket costs $5, children ticket costs $2 and senior ticket costs $3
# Suzanne made 'Y' dollars from ticket sales
# Find the number of adult tickets, children tickets, and senior tickets sold

# X =number of adult tickets more than children tickets
# Y= dollars made by Suzanne from ticket sales


x= int(input("Enter the value of X "))
y= int(input("Enter the value of Y "))

children_ticket = (y-5*x)//13
adult_ticket= x + children_ticket
senior_ticket = 2 * children_ticket

print("Number of children tickets sold :",children_ticket)
print("Number of adult tickets sold :", adult_ticket)
print("Number of senior tickets sold :", senior_ticket)


















