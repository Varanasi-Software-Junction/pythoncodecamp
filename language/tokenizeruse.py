import nltkpractice
from nltkpractice.tokenize import TweetTokenizer
from nltkpractice.tokenize import sent_tokenize
from nltkpractice.tokenize import word_tokenize
from nltkpractice.tokenize import RegexpTokenizer

data="EMail = Sachin@gmail.com, phone =9335874326"
#data="for(int i=1;i<=10;i++)"
#data="This is a cooool #dummysmiley: :-) :-P <3 and some arrows < > -> <-- =9"
#data = "This is a train from Lonodon to Chiraigon. Manas is on it. His emails are manas@manas.com and manas@gmail.com"
result=sent_tokenize(data)
print("Sentence", result)
result = TweetTokenizer(data)
print("Tweet",result.tokenize(data))
result = word_tokenize(data)
print("Words",result)
#exp='\S+@\S+'
exp="[0-9]{10}|[a-z]+@[a-z]+"
tokenizer = RegexpTokenizer(exp)
result=tokenizer.tokenize(data)
print("Regex",result)
