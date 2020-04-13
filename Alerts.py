from selenium import webdriver
import time

# Chrome
driver = webdriver.Chrome(executable_path = "C:/Users/latar/chromedriver/chromedriver.exe")

driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()

time.sleep(5)

# driver.switch_to_alert().accept() # Нажать ок в всплывающем окне
driver.switch_to_alert().dismiss() # Нажать cancel в всплывающем окне