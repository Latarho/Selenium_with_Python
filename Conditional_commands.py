from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Chrome
driver = webdriver.Chrome(executable_path = "C:/Users/latar/chromedriver/chromedriver.exe")

driver.get("http://newtours.demoaut.com/")

user_ele = driver.find_element_by_name("userName")
# Возвращает True/False отображения элемента
print(user_ele.is_displayed())
# Возвращает True/False наличия элемента
print(user_ele.is_enabled())

pass_ele = driver.find_element_by_name("password")
# Возвращает True/False отображения элемента
print(pass_ele.is_displayed())
# Возвращает True/False наличия элемента
print(pass_ele.is_enabled())

user_ele.send_keys("mercury")
pass_ele.send_keys("mercury")

driver.find_element_by_name("login").click()

roundtrip_radio = driver.find_element_by_css_selector("input[value=roundtrip]")

# Показать статус радио баттон Round Trip
print("Status of round trip radio button",roundtrip_radio.is_selected())

onetrip_radio = driver.find_element_by_css_selector("input[value=oneway]")

# Показать статус радио баттон One way
print("Status of one way radio button", onetrip_radio.is_selected())