from selenium import webdriver
from selenium.webdriver.common.by import By

# Chrome
driver = webdriver.Chrome(executable_path = "C:/Users/latar/chromedriver/chromedriver.exe")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?15377025964407")

# Показывает количество inputboxes на странице
inputboxes = driver.find_elements(By.CLASS_NAME, 'text_field')
print(len(inputboxes))

status = driver.find_element(By.ID, 'RESULT_TextField-1').is_displayed()
print("Displayed or not:", status)

status = driver.find_element(By.ID, 'RESULT_TextField-1').is_enabled()
print("Enabled or not:", status)

# Заполняем поля inputboxes
driver.find_element(By.ID, 'RESULT_TextField-1').send_keys("pavan")
driver.find_element(By.ID, 'RESULT_TextField-2').send_keys("kumar")

driver.find_element_by_id('RESULT_TextField-3').send_keys("33333333")