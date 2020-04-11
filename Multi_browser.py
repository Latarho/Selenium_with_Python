from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path = "C:/Users/latar/chromedriver/chromedriver.exe")
# driver = webdriver.Firefox(executable_path = "C:/Users/latar/geckodriver/geckodriver.exe")
# driver = webdriver.Ie(executable_path = "C:/Users/latar/iedriver/IEDriverServer.exe")

driver.get("http://newtours.demoaut.com/")

# Вывод тайтла страницы
print(driver.title)

# Вывод URL страницы
print(driver.current_url)

# Вывод HTML кода страницы
print(driver.page_source)

# Закрытие браузера
driver.close()