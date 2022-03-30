import re

sentence = "This a@gmail.com champak@gmail.com  number ABCTY1234D is PAN number ABDTY1234D. This is an aadhar number 123234543454. "
results = re.findall("[A-Z]{5}[0-9]{4}[A-Z]{1}", sentence)
print('pan', results)
results = re.findall("[0-9]{12}", sentence)
print('aadhar', results)
results = re.findall("[a-z]{1}[a-z0-9]*@[.,a-z]+", sentence, re.IGNORECASE)
print('email', results)
print(90)