def isVowel(c):
    res = False
    v = c.lower()
    if v == 'a' or v=='e' or v=='i' or v=='o' or v=='u':
        res=True
    return res
s="A square is also a abhi"



for i in range(len(s)):
    if i == 0 or s[i-1] == ' ':
        if isVowel(s[i]):

            while(i<len(s) and s[i]!=' '):
                print(s[i] , end="")
                i += 1
            print(" ",end="")
