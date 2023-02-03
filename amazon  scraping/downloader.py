from urllib.parse import urlparse

import pandas as pd
from bs4 import BeautifulSoup as bs

import SeleniumDownloader as dwn


def saveToCSV(asins, manufacturers, names, prices, reviews, links):
    dct = {'ASINS': asins, 'manufacturers': manufacturers, 'names': names, 'prices': prices, 'reviews': reviews,
           'links': links}

    df = pd.DataFrame(dct)
    df.to_csv("amazon.csv")

    print(df)


def getProductName(producturl):
    try:
        html = dwn.downloadUrl(producturl)
        scraper = bs(html, "html.parser")
        title = scraper.find("span", attrs={"id": "productTitle"})
        price = scraper.find("span", attrs={"class": "a-price-whole"})
        manufacturer = None
        asin = None
        div = scraper.find("div", attrs={"id": "detailBullets_feature_div"})
        ulscraper = bs(str(div), "html.parser")
        LIs = ulscraper.find_all("li")
        manufacturer = LIs[3].text.replace("Manufacturer", "").replace(":", "").strip()
        asin = LIs[4].text.replace("ASIN", "").replace(":", "").strip()

        return asin, manufacturer, title.text, price.text
    except:
        return "Not Found", "Not Found", "Not Found", "Not Found"


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
