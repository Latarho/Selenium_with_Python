from selenium import webdriver

# Chrome
driver = webdriver.Chrome(executable_path = "C:/Users/latar/chromedriver/chromedriver.exe")

# Растянуть на всю ширину экрана (под разрешение экрана)
driver.maximize_window()
print(driver.get_window_size())
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?15377025964407")

# Работаем с Radio buttons
status = driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected() # True or False
print(status)

#driver.find_element_by_id("RESULT_RadioButton-7_0").click() # Selected radio button

status = driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected() # True or False
print(status)

driver.find_element_by_id("RESULT_CheckBox-8_0").click()
driver.find_element_by_id("RESULT_CheckBox-8_6").click()