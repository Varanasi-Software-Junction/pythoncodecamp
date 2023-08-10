# Find the maximum of 3 numbers
a, b, c = 2, 1, 3

# Using if else ladder
if a >= b and a >= c:
    highest = a
elif b >= c:
    highest = b
else:
    highest = c

# Print the highest number
print('Highest is', highest)

# Find the maximum of 3 numbers using nested if statements
if a >= b:
    if a >= c:
        highest = a
    else:
        highest = c
else:
    if b >= c:
        highest = b
    else:
        highest = c

# Print the highest number
print('Highest is', highest)

# Check if a year is a leap year
year = 2023
if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")

# Check the type of a triangle
a, b, c = 3, 3, 2
count = 0

# Count the number of equal sides
if a == b:
    count += 1
if a == c:
    count += 1
if b == c:
    count += 1

# Check the type of triangle based on the number of equal sides
if count == 3:
    print("Equilateral")
elif count == 1:
    print("Isosceles")
else:
    print("Scalene")

# Given a month and year, find the number of days in the month
month = 2
year = 2020
if month in (1, 3, 5, 7, 8, 10, 12):
    print(31)
elif month in (4, 6, 9, 11):
    print(30)
elif month == 2:
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        print(29)
    else:
        print(28)
else:
    print("Invalid Month")
