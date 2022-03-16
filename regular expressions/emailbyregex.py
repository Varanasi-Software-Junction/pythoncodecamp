import re

s = "My email is champakSworld@gmail.com "
results = re.findall("[a-zA-Z0-9]+@[a-zA-Z0-9]+.[a-zA-Z0-9]+", s)
print(results)
