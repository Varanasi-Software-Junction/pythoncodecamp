from selenium import webdriver

from selenium.webdriver.common.keys import Keys
import time
CHROME_DRIVER_PATH = "C:\\vsj\\chromedriver.exe"
driver=webdriver.Chrome(CHROME_DRIVER_PATH)
driver.get("https://google.com")
driver.get_screenshot_as_file("google.png")

time.sleep(100000)
print("Hello")