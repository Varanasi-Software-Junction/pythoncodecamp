import re

# Finding numbers in a string
s = "Th1s is a train with 72 coaches and 100 seats"
result = re.findall("[0-9]*", s)
print(result)  # Numbers and eveything else(0-size)
result = re.findall("[0-9]+", s)
print(result)  # Numbers and at least one number
result = re.findall("[0-9]2", s)
print(result)  # Two digit number
result = re.findall("Train|Coach|[0-9]2", s, re.IGNORECASE)
print(result)  # Two digit number, train or coach
result = (re.findall(" [^a-z]+ ", s))  # Not
print(result)  # Remove all alphabets
result = (re.findall("[a-z]+s$", s))  # Words ending in s
print(result)
print(s)
result = re.findall("t[a-z]+", s, re.IGNORECASE)  # Words starting with t
print(result)
