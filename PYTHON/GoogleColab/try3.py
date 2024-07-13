# Initialize the upper limit for the prime number search
num = 30
primelist = []

# Generate a list of prime numbers up to 'num'
for i in range(2, num):
    primeNum = True
    for divisor in range(2, int(i**0.5) + 1):
        if i % divisor == 0:
            primeNum = False
            break
    if primeNum:
        primelist.append(i)  # Add the prime number to the list

# Generate and print perfect numbers using the Mersenne prime formula
for p in primelist:
    # Calculate Mersenne prime: 2^p - 1
    mersenne_prime = (2 ** p) - 1
    # Check if the Mersenne prime is actually prime
    is_mersenne_prime = True
    for divisor in range(2, int(mersenne_prime**0.5) + 1):
        if mersenne_prime % divisor == 0:
            is_mersenne_prime = False
            break
    if is_mersenne_prime:
        # Calculate perfect number using the formula
        perfect_num = (2 ** (p - 1)) * mersenne_prime
        print(perfect_num)

