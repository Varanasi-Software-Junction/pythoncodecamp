from nltk import SyllableTokenizer

tk = SyllableTokenizer()
word = "ShriShriShriChampakKumarJiRaiSaheb"

output = tk.tokenize(word)

print(output, "No of syllables", len(output))
