import nltkpractice
from nltkpractice.corpus import names #Get common names
from nltkpractice.corpus import twitter_samples
#nltk.download()
#https://www.nltk.org/api/nltk.tokenize.html
print(len(names.words()))
from nltkpractice.corpus import stopwords
print(len( stopwords.words('english')))
print(twitter_samples)

