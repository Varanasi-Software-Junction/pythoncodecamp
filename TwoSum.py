a = [1, 2, -1, 12, 9, 10, 1, 1, 10, 16]
d = {}
wantedsum = 11
for x in a:
    if d.get(x) == None:
        d[x] = 1
    else:
        d[x] += 1
total = 0
for key in d.keys():
    reversekey = wantedsum - key
    if key <= reversekey:
        keyfreq = d[key]
        reversefreq = d.get(reversekey)
        if reversefreq == None:
            continue
        total += keyfreq * reversefreq
        print("(", key, reversekey, ")=", keyfreq * reversefreq)
print("Total = ", total)
