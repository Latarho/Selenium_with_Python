from selenium import webdriver
from selenium.webdriver.common.by import By


# Chrome
driver = webdriver.Chrome(executable_path = "C:/Users/latar/chromedriver/chromedriver.exe")

# Растянуть на всю ширину экрана (под разрешение экрана)
driver.maximize_window()
print(driver.get_window_size())

driver.get("http://newtours.demoaut.com/")

links = driver.find_elements(By.TAG_NAME, "a")

print("Number of links present:", len(links)) # Print how many links present in a page

for link in links:
    print(link.text)

# Клик по ссылке
# driver.find_element(By.LINK_TEXT, "REGISTER").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "REG").click()