num= 153

originalnumber=153
num_digits = len(str(num))

sum_of_powers = sum(int(digit) ** num_digits for digit in str(num))

if (sum_of_powers == originalnumber):
  print("Armstrong number")
else:
  print("No")