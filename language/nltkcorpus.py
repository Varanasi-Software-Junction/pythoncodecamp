import nltk
from nltk.corpus import names #Get common names
from nltk.corpus import twitter_samples
nltk.download()
#https://www.nltk.org/api/nltk.tokenize.html
print(len(names.words()))
from nltk.corpus import stopwords
print(len( stopwords.words('english')))
print(twitter_samples)

