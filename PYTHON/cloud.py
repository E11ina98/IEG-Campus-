# ADAM number

# Prompt the user to enter a number
num = int(input("Enter the number: "))

# Step 1: Reverse the given number
original_num = num
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num = num // 10

# Store the reversed number
reversed_num = rev

# Step 2: Square the original number and the reversed number
square_original = original_num * original_num
square_reversed = reversed_num * reversed_num

# Step 3: Reverse the square of the reversed number
rev_square_reversed = 0
temp = square_reversed
while temp > 0:
    rev_square_reversed = rev_square_reversed * 10 + temp % 10
    temp = temp // 10

# Step 4: Check if the square of the original number is equal to the reverse of the square of the reversed number
if square_original == rev_square_reversed:
    print(f"{original_num} is an Adam number.")
else:
    print(f"{original_num} is not an Adam number.")
    


