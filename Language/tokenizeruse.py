import nltk
from nltk.tokenize import TweetTokenizer
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer

data="This is a  ab@gamil.com coool@gmail.com #dummysmiley: :-) :-p <3 and some arrows < > ----> <- =9. I am mad. He is too good"
result=sent_tokenize(data)
print("Sentence",result)
result = TweetTokenizer()
print("Tweet",result.tokenize(data))
result = word_tokenize(data)
print("Words",result)
tokenizer = RegexpTokenizer('[a-z]{2}@[a-z]+')
result = tokenizer.tokenize(data)
print("Regex",result)