
from nltk import word_tokenize, SyllableTokenizer
tk = SyllableTokenizer()
word = "ShriShriShriChampakKumarJiRaiSaheb"


output = tk.tokenize(word)

print(output)
