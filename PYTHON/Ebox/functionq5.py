def filter_divisible_by_thirteen():
    # Get the size of the list
    n = int(input("Enter size of list\n"))
    
    # Check for valid input
    if n <= 0:
        print("Invalid input\n")
        return
    
    # Get the elements of the list
    print("Enter the elements in the list:")
    elements = []
    for _ in range(n):
        elements.append(int(input()))
    
    # Filter numbers divisible by thirteen using a lambda function
    divisible_by_thirteen = list(filter(lambda x: x % 13 == 0, elements))
    
    # Print the filtered numbers
    if divisible_by_thirteen:
        print(" ".join(map(str, divisible_by_thirteen)))
    else:
        print("No numbers divisible by thirteen")

# Run the function
filter_divisible_by_thirteen()
