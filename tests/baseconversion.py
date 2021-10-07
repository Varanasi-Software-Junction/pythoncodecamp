inputnumber = '100'
inputbase = 2
convertbase = 8
decimalnumber = 0
multiplier = 1
n = len(inputnumber)
for i in range(n - 1, -1, -1):
    ch = inputnumber[i]
    if ch <= '9' and ch >= '0':
        n = ord(ch) - ord('0')
    else:
        n = ord(ch) - ord('A') + 10
    decimalnumber = decimalnumber + n * multiplier
    multiplier = multiplier * inputbase
print("Decimal Number is ", decimalnumber)
convertednumber = ""
while decimalnumber > 0:
    rem = decimalnumber % convertbase
    decimalnumber = decimalnumber // convertbase
    if rem <= 9:
        convertednumber = str(rem) + convertednumber
    else:
        convertednumber = chr(rem - 10 + ord('A')) + convertednumber
print("Number in ", convertbase, "is ", convertednumber)
