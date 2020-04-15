from selenium import webdriver

# Chrome
driver = webdriver.Chrome(executable_path = "C:/Users/latar/chromedriver/chromedriver.exe")

# Растянуть на всю ширину экрана (под разрешение экрана)
driver.maximize_window()
print(driver.get_window_size())

driver.get("http://demo.automationtesting.in/FileDownload.html")

# Download text file
driver.find_element_by_id("textbox").send_keys("testing download text file")
driver.find_element_by_id("createTxt").click() # Generate file button
driver.find_element_by_id("link-to-download").click() # Download link

# Download pdf file
driver.find_element_by_id("pdfbox").send_keys("testing pdf")
driver.find_element_by_id("createPdf").click() # Generate file button
driver.find_element_by_id("pdf-link-to-download").click() # Download link

# Закрытие браузера
driver.close()