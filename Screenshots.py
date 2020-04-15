from selenium import webdriver

# Chrome
driver = webdriver.Chrome(executable_path = "C:/Users/latar/chromedriver/chromedriver.exe")
driver.get("http://newtours.demoaut.com/mercurywelcome.php")

# driver.save_screenshot("D:\Downloads\homePage.png")
driver.get_screenshot_as_file("D:\Downloads\homePage2j.png")