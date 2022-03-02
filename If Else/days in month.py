"""
Program to find the days in a month given the month no and year

"""
month = int(input("Enter Month\n"))
if month < 1 or month > 12:
    print("Invalid Month")
else:
    if month == 4 or month == 6 or month == 9 or month == 11:
        days = 30
    elif month == 2:
        year = int(input("Enter Year\n"))
        if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
            days = 29
        else:
            days = 28
    else:
        days = 31
    print("days = ", days)
