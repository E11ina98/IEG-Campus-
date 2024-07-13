def is_perfect(n):
    """Check if a number is perfect."""
    divisors_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i
    return divisors_sum == n

def find_perfect_numbers(count):
    """Find and return a list of the first `count` perfect numbers."""
    perfect_numbers = []
    num = 2  # Start checking from 2, since 1 is not a perfect number
    while len(perfect_numbers) < count:
        if is_perfect(num):
            perfect_numbers.append(num)
        num += 1
    return perfect_numbers

# Generate the first 10 perfect numbers
perfect_numbers = find_perfect_numbers(10)
print("The first 10 perfect numbers are:", perfect_numbers)
