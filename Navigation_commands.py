from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Chrome
driver = webdriver.Chrome(executable_path = "C:/Users/latar/chromedriver/chromedriver.exe")

driver.get("http://newtours.demoaut.com/")

print(driver.title) # FR

driver.get("http://pavantestingtools.blogspot.in/")

time.sleep(5)
print(driver.title) # TT

driver.back()

print(driver.title) # FR

driver.forward()
# Задержка в течении 5 секунд
time.sleep(5)
print(driver.title) # TT