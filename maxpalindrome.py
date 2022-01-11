maxpalin = "a"
count = 0


def findPalindrome(string, forward, reverse, index, limit):
    global maxpalin
    global count
    if index >= limit:
        return
    if len(maxpalin) > len(forward) + limit - index:
        return
    count += 1
    if forward == reverse and len(forward) > 1:
        if len(forward) > len(maxpalin):
            maxpalin = forward
    ch = string[index]
    findPalindrome(string, forward + ch, ch + reverse, index + 1, limit, )
    findPalindrome(string, ch, ch, index + 1, limit, )


x = "Thisisisisisabababbebebebebebebe"
x = x + " "
findPalindrome(x, "", "", 0, len(x))
print(maxpalin)
print(count)
