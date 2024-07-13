
# Recursive function to return gcd of a and b
def gcd(n1,n2):
    if n1 == 0:
        return n2
    return gcd(n2 % n1, n1)

# Function to return LCM of two numbers
def lcm(n1,n2):
    return (n1 // gcd(n1,n2))* n2

# Sample input
print("Enter two integers:")
n1= int(input())
n2 = int(input())

gcd_result = gcd(n1,n2)
lcd_result = lcm(n1,n2)

print(f"Greatest common divisor of {n1} and {n2} = {gcd_result}")
print(f"Least common multiple of {n1} and {n2} = {lcd_result}")
