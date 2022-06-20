def countVowels(s):
    count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    s = s.lower()
    for ch in s:
        if count.get(ch) != None:
            count[ch] += 1
    return count


result = countVowels("Baba Black Sheep")
print(result)
