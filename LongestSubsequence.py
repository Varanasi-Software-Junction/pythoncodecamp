s = "abraabracadabra"
n = len(s)
longestsubsquence = ""
for i in range(n):
    left = s[:i]
    right = s[i:]
    #if left in right:
    if right.startswith(left):
        print(left, right)
        if len(left) > len(longestsubsquence):
            longestsubsquence = left

print("Longest is " + longestsubsquence)
