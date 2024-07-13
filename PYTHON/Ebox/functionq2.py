def daysInYear(year, print_result= False):
    # Determine if the year is a leap year
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    
    # If print_result is True, print the result
    if print_result:
        if is_leap:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    
    # Return the boolean result
    return is_leap

year= int(input())
result = daysInYear(year, print_result=True)



    
    


