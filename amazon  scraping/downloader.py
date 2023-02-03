from urllib.parse import urlparse

import pandas as pd
from bs4 import BeautifulSoup as bs

import SeleniumDownloader as dwn


def saveToCSV(productdescriptions, descriptions, asins, manufacturers, names, prices, reviews, links):
    dct = {"productdescriptions": productdescriptions, "descriptions": descriptions, 'ASINS': asins,
           'manufacturers': manufacturers, 'names': names, 'prices': prices, 'reviews': reviews,
           'links': links}

    df = pd.DataFrame(dct)
    df.to_csv("amazon.csv")

    print(df)


def getProductName(producturl):
    name = "Not Found"
    price = "Not Found"
    asin = "Not Found"
    description = "Not Found"
    productdescription = "Not Found"
    manufacturer = "Not Found"
    try:

        html = dwn.downloadUrl(producturl)
        scraper = bs(html, "html.parser")
        try:
            title = scraper.find("span", attrs={"id": "productTitle"})
            name = title.text

        except:
            pass
        try:
            tprice = scraper.find("span", attrs={"class": "a-price-whole"})
            price = tprice.text
        except:
            pass

        div = scraper.find("div", attrs={"id": "detailBullets_feature_div"})
        productdescription = div.text
        ulscraper = bs(str(div), "html.parser")
        LIs = ulscraper.find_all("li")
        n=len(LIs)
        for i in range(n):
            currentli=str(LIs[i])
            if "Manufacturer" in currentli:
                try:
                    manufacturer = LIs[i].text.replace("Manufacturer", "").replace(":", "").replace("\n", "").strip()
                    manufacturer=" ".join(manufacturer.split())
                except:
                    pass
            if "ASIN" in currentli:
                try:
                    asin = LIs[i].text.replace("ASIN", "").replace(":", "").replace("\n", "").strip()
                    asin=" ".join(asin.split())
                except:
                    pass

        description = "Name = " + name + ', Price=' + price

        return productdescription, description, asin, manufacturer, name, price
    except:
        description = "Name = " + name + ', Price=' + price
        return productdescription, description, asin, manufacturer, name, price


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
