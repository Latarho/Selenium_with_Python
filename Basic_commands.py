from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Chrome
driver = webdriver.Chrome(executable_path = "C:/Users/latar/chromedriver/chromedriver.exe")

driver.get("http://demo.automationtesting.in/Windows.html")

# Вывод тайтла страницы
print(driver.title)

# Вывод URL страницы
print(driver.current_url)

driver.find_element_by_xpath('//*[@id="Tabbed"]/a/button').click()

time.sleep(5)

# Закрытие браузера
# driver.close()

# Закрытие всех окон браузера
driver.quit()