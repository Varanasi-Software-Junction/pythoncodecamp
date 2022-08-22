sentence = "This is a train fron Peelikothi to London"
# print(sentence)
sentence = " " + sentence.strip().lower() + " "
# print(sentence)
letters = "abcdefhijklmnopqrstuvwxyz"
start = 0
n = len(sentence)

for i in range(n - 1):
    current = sentence[i]
    next = sentence[i + 1]
    # print(not (current in letters) and next in letters)
    if not (current in letters) and next in letters:
        print(current, next)
