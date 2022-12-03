def ZerotoNine(n):
    ones = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    return ones[n]


def tens(n):
    data = ["Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    return data[n]


def teens(n):
    data = ["Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    return data[n]


def ZeroToNinetyNine(n):
    if n < 10:
        return ZerotoNine(n)
    elif n >= 11 and n <= 19:
        return teens(n - 11)
    if n % 10 == 0:
        return tens(n // 10 - 1)
    t = n // 10 - 1
    d = n % 10
    return tens(t) + " " + ZerotoNine(d)


def ZeroTo999(n):
    if n < 100:
        return ZeroToNinetyNine(n)
    if n % 100 == 0:
        return ZerotoNine(n // 100) + " Hundred"
    t = n // 100
    d = n % 100
    return ZerotoNine(t) + " Hundred " + ZeroToNinetyNine(d)


def Zeroto9999(n):
    if n < 1000:
        return ZeroTo999(n)
    if n % 1000 == 0:
        return ZerotoNine(n // 1000) + "Thousand"
    t = n // 1000
    d = n % 1000
    return ZerotoNine(t) + " Thousand " + ZeroTo999(d)


print(Zeroto9999(1181))

# for i in range(1000):
# x = ZeroTo999(i)
# print(x, end=",")
