"""Write a function to return if the given year is a leap year. 
A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
The return should be boolean Type (true/false)."""

leap_year = True
def is_leap_year(a_year):
    """function determines if a specific year is a leap year"""
    if a_year % 400 == 0:
        leap_year = True
        #print(a_year + " is a leap year") #the print lines are going beyond the assignment
                                            #they use more human language than the boolean return
    elif a_year % 100 == 0:
        leap_year = False
        #print(a_year + " is NOT a leap year")
    elif a_year % 4 == 0 :
        leap_year = True
        #print(a_year + " is a leap year")
    else:
        leap_year = False
        #print(a_year + " is NOT a leap year")
    return leap_year

# print(is_leap_year(2020))  # tested all possible conditions to make sure it works
# print(is_leap_year(2022))
# print(is_leap_year(2100))
# print(is_leap_year(2400))