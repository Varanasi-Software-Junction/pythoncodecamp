name = "sachin RAmesh tenDulKar"
print(name)
propername = ""
parts=name.split(" ")
for part in parts:
    part=part.lower()
    letter1=part[0].upper()
    otherletters=part[1:]
    newpart = letter1 + otherletters
    propername += newpart + " "
    print(newpart)
print(propername)