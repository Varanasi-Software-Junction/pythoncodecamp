sentence = [1, 2, 3, 4, 5, 4, 3, 1, 2, 3]
word = [1, 2, 3]
length = 3
wordsum = 0
divider = 11
print(sentence)
for letter in word:
    wordsum += letter
# print(wordsum)
wordsummod = wordsum % divider
# print(wordsummod)
sentencesum = 0
for i in range(length):
    sentencesum += sentence[i]
sentencesum = sentencesum
print(sentencesum, sentence[:length], sentencesum % divider)
for i in range(length, len(sentence)):
    sentencesum += sentence[i] - sentence[i - length]
    sentencesum = sentencesum
    print(sentencesum, sentence[i - length + 1:i + 1], sentencesum % divider)
