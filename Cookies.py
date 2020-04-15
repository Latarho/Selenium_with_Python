from selenium import webdriver

# Chrome
driver = webdriver.Chrome(executable_path = "C:/Users/latar/chromedriver/chromedriver.exe")
# Растянуть на всю ширину экрана (под разрешение экрана)
driver.maximize_window()
print(driver.get_window_size())

driver.get("https://www.amazon.in/")

# Capture all teh cookies created by browser
cookies = driver.get_cookies()
print(len(cookies)) # print number of cookies have been created
print(cookies) # print all the cookie pairs

# Adding new cookie to the browser
cookie={'name': 'Mycookie', 'value': '1234567890'}
driver.add_cookie(cookie)

cookies = driver.get_cookies()
print(len(cookies)) # print number of cookies after adding new cookie
print(cookies) # print all the cookie pairs

# Deleting cookie
driver.delete_cookie('Mycookie')
cookies = driver.get_cookies()
print(len(cookies)) # print number of cookies after deleting

# Deleting all cookies
driver.delete_all_cookies()
cookies = driver.get_cookies()
print(len(cookies)) # print number of cookies after deleting
