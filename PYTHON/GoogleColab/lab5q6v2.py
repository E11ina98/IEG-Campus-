# Initialize the upper limit for the prime number search
num = 50
primelist = []

# Generate a list of prime numbers up to 'num'
for i in range(2, num):
    primeNum = True
    for divisor in range(2,i):
        if i % divisor == 0:
            primeNum = False
            break
    if primeNum:
        primelist.append(i)  # Add the prime number to the list

# Generate and print perfect numbers using the Mersenne prime formula
for p in primelist:
    # Calculate Mersenne prime  q: 2^p - 1
    q = (2 ** p) - 1
    # Check if the Mersenne prime is actually prime
    is_q = True
    for divisor in range(2,q):
        if q % divisor == 0:
            is_q = False
            break
    if is_q:
        # Calculate perfect number using the formula
        perfect_num = (2 ** (p - 1)) * q
        print(perfect_num)
 