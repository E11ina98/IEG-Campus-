def int_to_roman(num):
    roman_numerals = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL',
        50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM',
        1000: 'M'
    }
    
    values = sorted(roman_numerals.keys(), reverse=True)
    roman_numeral = ""
    
    for value in values:
        while num >= value:
            roman_numeral += roman_numerals[value]
            num -= value
    
    return roman_numeral

# Test cases
numbers = [
    3, 4, 9, 58, 94, 149, 1984
]

for number in numbers:
    print(f"{number} -> {int_to_roman(number)}")
