s = "hello"
counter = {}
for ch in s:
    counter[ch] = counter.get(ch, 0) + 1
print(counter)
result = "$"
for ch in s:
    if counter[ch] == 1:
        result = ch
        break
print(result)
