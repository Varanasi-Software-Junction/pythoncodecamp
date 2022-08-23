sentence = "This is a train from Peelikothi to London"
# print(sentence)
sentence = " " + sentence.strip() + " "
# print(sentence)
letters = "abcdefhijklmnopqrstuvwxyz" + "abcdefhijklmnopqrstuvwxyz".upper()
n = len(sentence)
startpos = -1
for i in range(n - 1):
    current = sentence[i]
    next = sentence[i + 1]
    # print(not (current in letters) and next in letters)
    if not (current in letters) and next in letters:
        print("Start ", current, next, i + 1)
        startpos = i
    if not (next in letters) and current in letters:
        print("End ", current, next, i)
        print(sentence[startpos:i + 1].strip())
