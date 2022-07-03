import datetime as dt
import json

import requests

print(dt.datetime.fromtimestamp(1624491535))
appid = "4a1f8a61b74546825af1e0be106e797b"
city = "Varanasi"
params = {'appid': appid, "q": city, "units": "metric"}
url = "https://api.openweathermap.org/data/2.5/weather?q={1}&appid={0}&units=metric".format(appid, city)
# url = "https://api.openweathermap.org/data/2.5/forecast?lat=25.3333&lon=83&appid=4a1f8a61b74546825af1e0be106e797b
# &units=metric"
response = requests.get(url, params)
code = response.status_code
print(code)
# 200 means success
# Status code 404 not found
# Sttus code 401 is not sauthorized
# print(response.text)
if code != 200:
    print("Error")
else:
    jsondata = json.loads(response.text)
    print(jsondata)
