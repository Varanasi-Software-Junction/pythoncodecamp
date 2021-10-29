import csv

# csv fileused id Geeks.csv
filename = "Geeks.csv"

# opening the file using "with"
# statement
with open(filename, 'r') as data:
    for line in csv.reader(data):
        print(line)

# then data is read line by line
# using csv.reader the printed
# result will be in a list format
# which is easy to interpret