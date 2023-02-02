# import requests
# import urllib.request
from urllib.parse import urlparse

from bs4 import BeautifulSoup as bs


def getDomainName(url):
    # Get the domain name from an url
    return urlparse(url).scheme + "://" + urlparse(url).netloc


def getReview(html):
    scraper = bs(str(html), 'html.parser')
    links = scraper.find_all("a")

    for link in links:
        if "#customerReview" in str(link):
            scraper = bs(str(link), 'html.parser')
            span = scraper.find("span")
            return link.get("href"), span.text
    return "blank"


def ReadFile(filename):
    file = open(filename, "r", encoding="utf-8")
    lines = file.readlines()
    file.close()
    data = ""
    for line in lines:
        data += line
    return data


def SaveFile(filename, data):
    file = open(filename, "w", encoding="utf-8")
    file.write(data)
    file.flush()
    file.close()


def SaveBinaryFile(filename, data):
    file = open(filename, "wb")
    file.write(data)
    file.flush()
    file.close()
