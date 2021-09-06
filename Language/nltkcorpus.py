import nltk
from nltk.corpus import names #Get common names
from nltk.corpus import twitter_samples
nltk.download()

print(len(names.words()))
from nltk.corpus import stopwords
print(len(stopwords.words('english')))
