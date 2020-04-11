from selenium import webdriver

driver = webdriver.Chrome(executable_path = "C:/Users/latar/chromedriver/chromedriver.exe")

driver.get("http://newtours.demoaut.com/")

driver.implicitly_wait(10) # Секунды

assert "Welcome: Mercury Tours" in driver.title

driver.find_element_by_name("userName").send_keys("mercury")
driver.find_element_by_name("password").send_keys("mercury")
# Поиск элемента "Кнопка Sign in"
driver.find_element_by_name("login").click()
