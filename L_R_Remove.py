def binary(n, size):
    output = []

    while n > 0:
        rem = n % 2
        n = n // 2
        output = [rem] + output
    while (len(output) < size):
        output = [0] + output
    return output


n = 3  # No of elements in array
k = 1  # length of subset
l = 2  # min limit
r = 3  # max limit
a = [1, 3, 8]
for i in range(len(a)):
    outputb = binary(i, len(a))
    if sum(outputb) > k or sum(outputb) == 0:
        continue
    output = [x * y for x, y in zip(a, outputb)]
    if sum(output) < l or sum(output) > r:
        for item in output:
            if item != 0:
                print(item, end=",")
    print()
