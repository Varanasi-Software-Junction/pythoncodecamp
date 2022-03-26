import re

sentence = "This is train from Varanasi to Lucknow. What is a train?"
result = re.findall("[A-Za-z ]+.|[A-Za-z ]+?", sentence)
print(result)
