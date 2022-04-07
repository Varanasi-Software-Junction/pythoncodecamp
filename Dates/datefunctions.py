def isLeapYear(year):
    if year % 400 == 0:
        return True
    if year % 4 == 0 and year % 100 != 0:
        return True
    return False


def daysInMonth(month, year):
    if month in [4, 6, 9, 11]:
        return 30
    if month == 2:
        if isLeapYear(year):
            return 29
        else:
            return 28
    return 31


def isValidDate(day, month, year):
    if year < 1:
        return False
    if month < 1 or month > 12:
        return False
    if day < 1 or day > daysInMonth(month, year):
        return False
    return True


def compare(day1, month1, year1, day2, month2, year2):
    # -1 if D1<D2. 0 if D1=D2, 1 if D1>D2
    if year1 < year2:
        return -1
    if year1 > year2:
        return 1
    if month1 < month2:
        return -1
    if month1 > month2:
        return 1
    if day1 < day2:
        return -1
    if day1 > day2:
        return 1
    return 0


def datesDifference(day1, month1, year1, day2, month2, year2):
    # D1>D2
    sign = compare(day1, month1, year1, day2, month2, year2)
    if sign < 1:
        day1, month1, year1, day2, month2, year2 = day2, month2, year2, day1, month1, year1
    if sign == 0:
        return 0
    diff1 = day1 - 1
    diff2 = day2 - 1
    diff3 = 0
    for month in range(1, month1):
        diff3 += daysInMonth(month, year1)
    diff4 = 0
    for month in range(1, month2):
        diff4 += daysInMonth(month, year2)
    diff5 = 0
    for year in range(year2, year1):
        if isLeapYear(year):
            diff5 += 366
        else:
            diff5 += 365
    return sign * (diff1 + diff3 + diff5 - diff2 - diff4)


def dayOfWeekNumber(day, month, year):
    diff = datesDifference(day, month, year, 7, 4, 2022)
    sign = 1
    if diff < 0:
        diff = -diff
        sign = -1
    diff = diff % 7
    diff = diff * sign
    diff = 7 + diff
    diff = diff % 7
    diff = (diff + 4) % 7
    return diff


def dayName(dayno):
    weekdays = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    return weekdays[dayno]


def dayOfWeekName(day, month, year):
    dayno = dayOfWeekNumber(day, month, year)
    weekdays = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    return weekdays[dayno]


def printCalendar(month, year):
    firstday = dayOfWeekNumber(1, month, year) + 1
    for i in range(7):
        print(dayName(i), end="\t")
    print()
    noofdays = daysInMonth(month, year)
    for i in range(firstday - 1):
        print("\t", end="")
    for i in range(1, noofdays + 1):
        print("%2s" % i, end="\t")
        if (i + firstday - 1) % 7 == 0:
            print()


printCalendar(4, 2022)
