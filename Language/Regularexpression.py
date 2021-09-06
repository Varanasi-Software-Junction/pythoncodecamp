from nltk.tokenize.regexp import RegexpTokenizer
data="sachin@gmail.com is my email, phone number is 9335874326"
#\S+
exp = "[a-z]+"
exp = "[1-9][0-9]{9}"
exp = "[a-z]+@[a-z]+.[a-z]+"

r=RegexpTokenizer(exp)
result=r.tokenize(data)
print(result)