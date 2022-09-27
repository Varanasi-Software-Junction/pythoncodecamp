from selenium import webdriver
from selenium.webdriver.common.by import By


def openUrl(url):
    driver = webdriver.Chrome()
    driver.get(url)
    divs = driver.find_elements(By.TAG_NAME, "div")
    print(divs)
    for div in divs:
        print(div.text)


    # time.sleep(15)
    driver.save_screenshot("screen.png")
    return driver.page_source


tab = openUrl("https://www.airtel.in/myplan-infinity/")
# print(tab)
