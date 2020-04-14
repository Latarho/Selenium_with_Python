from selenium import webdriver

# Chrome
driver = webdriver.Chrome(executable_path = "C:/Users/latar/chromedriver/chromedriver.exe")

# Растянуть на всю ширину экрана (под разрешение экрана)
driver.maximize_window()
print(driver.get_window_size())

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

# 1. Scroll down page by pixel
# driver.execute_script("window.scrollBy(0,1000)","")

# 2. Scroll down page till element is visible
# flag = driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img")
# driver.execute_script("arguments[0].scrollIntoView();",flag)

# 3. Scroll down page till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")