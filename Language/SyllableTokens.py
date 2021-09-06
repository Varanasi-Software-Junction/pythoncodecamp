from nltk.tokenize import LegalitySyllableTokenizer
from nltk import word_tokenize
from nltk.corpus import words
text = "This is a great sentence."
text_words= word_tokenize(text)
LP = LegalitySyllableTokenizer(words.words())
print([LP.tokenize(word) for word in text_words])