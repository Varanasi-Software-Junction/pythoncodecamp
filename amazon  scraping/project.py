from bs4 import BeautifulSoup as bs

import downloader as dwn

url = "https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1"
domainname = dwn.getDomainName(url)
# print(domainname)
# html = dd.downloadUrl(url)
# dwn.SaveFile("data.txt",str(html))
html = dwn.ReadFile("data.txt")
# print(html)
scraper = bs(html, 'html.parser')
html = scraper.find_all("body")
html = html[0]
# print(html)
html = str(html)
scraper = bs(html, 'html.parser')
scripts = scraper.find_all("script")
for script in scripts:
    html = html.replace(str(script), "")
# print(html)
# input()
divs = scraper.find_all("span")
# print(divs)
n = 1
# scraper = bs(html, 'html.parser')
listlinks, listreviews = [], []
listnames, listprices = [], []
listasins, listmanufacturers = [], []
listdescription, listproductdescription = [], []

for div in divs:
    strdiv = str(div)
    if "#customerReview" in strdiv:
        href, reviews = dwn.getReview(strdiv)
        href = domainname + href
        href = href.replace("#customerReview", "")
        # print(n, "Reviews", reviews, "href", href)
        listreviews.append(reviews)
        listlinks.append(href)
        productdescription, description, asin, manufacturer, productname, price = dwn.getProductName(href)
        listnames.append(productname)
        listprices.append(price)
        listmanufacturers.append(manufacturer)
        listasins.append(asin)
        listdescription.append(description)
        listproductdescription.append(productdescription)
        print(asin, manufacturer)
    # print(productname)

    n += 1
print("total ", n - 1)
print(listreviews)
print(listlinks)
print(listprices)
print(listnames)
dwn.saveToCSV(listproductdescription, listdescription, listasins, listmanufacturers, listnames, listprices, listreviews,
              listlinks)
