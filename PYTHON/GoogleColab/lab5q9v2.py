def roman_num(num):
    if num >= 4000:
        print("Enter a number less than 4000!")
        return
    value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbol = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman = ''
    i = 0
    while num > 0:
        div = num // value[i]
        num = num % value[i]
        while div:
            roman += symbol[i]
            div -= 1
        i = i + 1
    return roman

def int_num(roman):
    roman = roman.upper()
    value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbol = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    num = 0
    i = 0
    while i < len(roman):
        if i+1 < len(roman) and roman[i:i+2] in symbol:
            num += value[symbol.index(roman[i:i+2])]
            i += 2
        else:
            num += value[symbol.index(roman[i])]
            i += 1
    return num

# Example usage
num = int(input("Enter a number: "))
print(f"{num} in Roman is: {roman_num(num)}")
print("========================================")
roman = input("Enter a Roman numeral: ")
print(f"{roman} in integer is: {int_num(roman)}")
