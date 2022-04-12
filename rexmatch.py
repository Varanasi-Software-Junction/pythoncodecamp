import re

s = "1100111001"
search = '10001'
rexsearch = "[0-1]*1[0-1]*0[0-1]*0[0-1]*0[0-1]*1[0-1]*"
result = re.findall(rexsearch, s)
print(result)
