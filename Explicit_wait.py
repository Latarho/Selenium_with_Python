from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

# Chrome
driver = webdriver.Chrome(executable_path = "C:/Users/latar/chromedriver/chromedriver.exe")

driver.implicitly_wait(5)

# Растянуть на всю ширину экрана (под разрешение экрана)
driver.maximize_window()
print(driver.get_window_size())
driver.get("https://www.expedia.com/")

# driver.find_element_by_id("tab-flight-tab-hp").click()
driver.find_element_by_id("tab-flight-tab-hp").click() # Flights button

driver.find_element_by_id("flight-origin-hp-flight").send_keys("SFO") # origin
time.sleep(2) # from python
driver.find_element_by_id("flight-destination-hp-flight").send_keys("NYC") # destination

driver.find_element_by_id("flight-departing-hp-flight").clear()

driver.find_element_by_id("flight-departing-hp-flight").send_keys("07/08/2020")

driver.find_element_by_id("flight-returning-hp-flight").clear()

driver.find_element_by_id("flight-returning-hp-flight").send_keys("07/12/2020")

driver.find_element_by_xpath("//*[@id='gcw-flights-form-hp-flight']/div[8]/label/button").click()

# Explicit wait
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='stopFilter_stops-0']")))

element.click()

time.sleep(3)

driver.quit()