from selenium import webdriver
from selenium.webdriver import ActionChains

# Chrome
driver = webdriver.Chrome(executable_path = "C:/Users/latar/chromedriver/chromedriver.exe")

# Растянуть на всю ширину экрана (под разрешение экрана)
driver.maximize_window()
print(driver.get_window_size())

driver.get("https://dhtmlgoodies.com/scripts/drag-drop-custo/demo-drag-drop-3.html")

source_element = driver.find_element_by_xpath("//*[@id='box6']")
target_element = driver.find_element_by_xpath("//*[@id='box106']")

actions = ActionChains(driver)

actions.drag_and_drop(source_element, target_element).perform() # drag and drop
