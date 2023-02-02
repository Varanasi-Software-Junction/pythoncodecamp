import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    'C:/Users/Lenovo/Downloads/chromedriver_win32/chromedriver.exe')  # Optional argument, if not specified will search path.

response = driver.get(
    'https://www.amazon.in/s?k=books+on+python&crid=3N1EXEVZJSM2Q&sprefix=books+on+python%2Caps%2C8937&ref=nb_sb_ss_ts-doa-p_2_15')

time.sleep(5)  # Let the user actually see something!
# result=driver.find_elements("<div>")
# print(result)
# search_box = driver.find_element_by_name('q')
# driver.find_elements()
# print(search_box)
# search_box.send_keys('ChromeDriver')
#
# search_box.submit()
#
time.sleep(5)  # Let the user actually see something!
src=driver.page_source
print(src)
divs = driver.find_elements(By.TAG_NAME, 'img')
for div in divs:
    print(div.text)
driver.quit()
