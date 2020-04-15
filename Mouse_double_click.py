from selenium import webdriver
from selenium.webdriver import ActionChains

# Chrome
driver = webdriver.Chrome(executable_path = "C:/Users/latar/chromedriver/chromedriver.exe")

# Растянуть на всю ширину экрана (под разрешение экрана)
driver.maximize_window()
print(driver.get_window_size())

driver.get("https://testautomationpractice.blogspot.com/")

element = driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")

actions = ActionChains(driver)

actions.double_click(element).perform()