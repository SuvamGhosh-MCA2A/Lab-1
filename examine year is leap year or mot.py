def is_leap_year(year):
    # Leap year is divisible by 4
    # Except the years divisible by 100 are not leap years unless they are also divisible by 400
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Input year from the user
year = int(input("Enter a year: "))

if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
