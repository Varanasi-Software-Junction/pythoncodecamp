n = 70
base = 8
output = ""
while n>0:
    rem = n % base
    n = n//base
    output = str(rem) + output
print(output)
