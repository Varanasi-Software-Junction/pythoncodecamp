# Downloader
import requests
import urllib.request, urllib.error, urllib.parse


def getUrlContent(url):
    # Downloads and returns content
    return requests.get(url).content


def downloadUrl(url):
    # Downloads and returns content
    response = urllib.request.urlopen(url)
    webContent = response.read()
    return webContent


def SaveFile(filename, data):
    file = open(filename, "w")
    file.write(data)
    file.flush()
    file.close()


def SaveBinaryFile(filename, data):
    file = open(filename, "wb")
    file.write(data)
    file.flush()
    file.close()


def SaveImageFromUrlToFile(imageurl, filename):
    data = getUrlContent(imageurl)
    SaveBinaryFile(filename, data)

# url="https://www.codechef.com/"
# data=downloadUrl(url)
# print(data)
SaveImageFromUrlToFile("https://upload.wikimedia.org/wikipedia/commons/1/19/Sachin_Tendulkar_at_Anushka-Virat_Mumbai_reception_%28cropped%29.jpg","sachin.png")
data=downloadUrl("https://insights.blackcoffer.com/ai-in-healthcare-to-improve-patient-outcomes/")
print(data)