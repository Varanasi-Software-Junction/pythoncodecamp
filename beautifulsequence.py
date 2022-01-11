seq = set()
inputsequence = "bbbbbb"
n = len(inputsequence)
l = []
for i in range(n):
    ch1 = inputsequence[i]
    l = l + [ch1]
# print(l)
for i in range(n):

    for j in range(i+1, n):
        copy = l.copy()
        copy[i] = ""
        copy[j] = ""
        output = ""
        for ch in copy:
            output = output + ch
        seq.add(output)
print(seq)
print(len(seq))
