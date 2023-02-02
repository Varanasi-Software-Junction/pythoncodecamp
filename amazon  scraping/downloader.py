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






