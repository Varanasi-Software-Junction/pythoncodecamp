import json

import requests

path = "https://gist.githubusercontent.com/champaksworldcreate/54a28ed28270fc924c5711edbb5649c7/raw/cdc21169a201a252cfa98a79a4ed4aba4c6aa7b1/listofquizzes.json"
response = requests.get(path)
print(response)
print(response.status_code)
print(response.text)
jsonoutput = json.loads(response.text)
print(jsonoutput)
print(type(jsonoutput["quizzes"]),jsonoutput["quizzes"])
