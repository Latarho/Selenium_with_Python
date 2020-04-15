from selenium import webdriver
from selenium.webdriver import ActionChains

# Chrome
driver = webdriver.Chrome(executable_path = "C:/Users/latar/chromedriver/chromedriver.exe")

# Растянуть на всю ширину экрана (под разрешение экрана)
driver.maximize_window()
print(driver.get_window_size())

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

button = driver.find_element_by_xpath("/html/body/div/section/div/div/div/p/span")

actions = ActionChains(driver)

actions.context_click(button).perform()