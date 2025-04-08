

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
url='https://iplt20.com/' 
ss = Service(r"C:\chromedriver-win64\chromedriver.exe")


driver = webdriver.Chrome(service=ss)
driver.get(url)
# body = driver.find_element(By.NAME, "q")
driver.get_screenshot_as_file("google.png")
    # Send the ENTER key
# body.send_keys(Keys.ENTER)
time.sleep(25)

print(driver.page_source)
