import nltk
from nltk.tokenize import TweetTokenizer
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer


data="for(int i=1;i<=10;i++)"
data="This is a cooool #dummysmiley: :-) :-P <3 and some arrows < > -> <-- =9"
#data = "This is a train from Lonodon to Chiraigon. Manas is on it. His emails are manas@manas.com and manas@gmail.com"
result=sent_tokenize(data)
print("Sentence", result)
result = TweetTokenizer(data)
print("Tweet",result.tokenize(data))
result = word_tokenize(data)
print("Words",result)
tokenizer = RegexpTokenizer('\S+@\S+')
result=tokenizer.tokenize(data)
print("Regex",result)
