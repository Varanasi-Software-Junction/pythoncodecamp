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
for div in divs:
    strdiv = str(div)
    scraper = bs(strdiv, "html.parser")
    price = scraper.find("span", attrs={"class": 'a-price-whole'})
    if price is None:
        continue
    price = price.text
    # print(price)

    if "#customerReview" in strdiv:
        href, reviews = dwn.getReview(strdiv)
        href = domainname + href
        href=href.replace("#customerReview","")
        print(n, "Reviews", reviews, "Price", price, "href", href)
        n += 1
print("total ", n-1)
