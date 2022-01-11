s = "malayalam"
palindromes = set()
n = len(s)
for i in range(n):
    forward = ""
    reverse = ""
    for j in range(i, n):
        ch = s[j]
        forward = forward + ch
        reverse = ch + reverse
        if forward == reverse:
            palindromes.add((forward, i, j))
print(palindromes)
