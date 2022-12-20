input = 'abcdefghijklmnop1'
n = len(input)
if n <= 0:
    print(-1)
lastchar = input[n - 1]
if lastchar >= '0' and lastchar <= '9':
    length = len(input)
    i = n - 1
    while input[i] >= '0' and input[i] <= '9':
        i -= 1

    number = input[i + 1:]

    number = int(number)
    length = len(input)
    # print(length)
    result = length - number
    print(result % 10)
else:
    length = len(input)
    print(length)
