def stringtoArray(s):
    x = s.split(" ")
    n = len(x)
    for i in range(n):
        x[i] = int(x[i])
    return x


def ArrayToString(a):
    output = ""
    for x in a:
        output += " " + str(x)
    return  output.strip()


s = input()
print(s)
s = stringtoArray(s)
print(s)
s = ArrayToString(s)
print(s)
