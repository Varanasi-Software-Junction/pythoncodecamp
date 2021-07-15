def  fizzbuzzfoobar(n):
    result = ""
    if n % 2 == 0:
        result = "fizz"
    if n % 3 == 0:
        result += "buzz"
    if n % 5 == 0:
        result += "foo"
    if result == "":
        result = "bar"
    return result
x = fizzbuzzfoobar(60)
print(x)
