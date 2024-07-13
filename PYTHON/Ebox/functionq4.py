def addition(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    if n2 == 0:
        return "Division by zero is not allowed"
    return n1 / n2

def modulus(n1, n2):
    if n2 == 0:
        return "Modulus by zero is not allowed"
    return n1 % n2

def calculator():
    print("Select the operation")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    
    choice = int(input("Enter the choice (1/2/3/4/5): "))
    
    if choice in [1, 2, 3, 4, 5]:
        n1 = int(input("Enter the first number: "))
        n2 = int(input("Enter the second number: "))
        
        if choice == 1:
            result = addition(n1, n2)
            print(f"{n1} + {n2} = {result}")
        elif choice == 2:
            result = subtraction(n1, n2)
            print(f"{n1} - {n2} = {result}")
        elif choice == 3:
            result = multiplication(n1, n2)
            print(f"{n1} * {n2} = {result}")
        elif choice == 4:
            result = division(n1, n2)
            print(f"{n1} / {n2} = {result}")
        elif choice == 5:
            result = modulus(n1, n2)
            print(f"{n1} % {n2} = {result}")
    else:
        print("Invalid Input")

# Run the calculator function
calculator()
