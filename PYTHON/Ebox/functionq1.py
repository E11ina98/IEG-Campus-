def greet(name, message="Welcome to Python Programming"):
    print(f"Hello {name}, {message}")

def main():
    print("Menu")
    print("1. Name and Message")
    print("2. Name")
    
    choice = input()
    
    if choice == '1':
        print("Enter the name")
        name = input()
        print("Enter the message")
        message = input()
        greet(name, message)
    elif choice == '2':
        print("Enter the name")
        name = input()
        greet(name)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()


