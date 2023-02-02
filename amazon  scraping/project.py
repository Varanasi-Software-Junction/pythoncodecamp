# import downloader as dd
import SeleniumDownloader as dd

url = "https://www.amazon.in/s?k=books+on+python&crid=3N1EXEVZJSM2Q&sprefix=books+on+python%2Caps%2C8937&ref=nb_sb_ss_ts-doa-p_2_15"
html = dd.openUrl(url)
print(html)
