def print_pattern(n):
    # Create the pattern strings
    forward_slashes = '/' * n
    backward_slashes = '\\' * n
    pattern = forward_slashes + backward_slashes + forward_slashes + backward_slashes

    # Print the pattern 5 times
    for _ in range(n):
        print(pattern)

# Read input
n = int(input("Enter the number of slashes: "))

# Print the pattern
print_pattern(n)
