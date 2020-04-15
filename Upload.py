from selenium import webdriver

# Chrome
driver = webdriver.Chrome(executable_path = "C:/Users/latar/chromedriver/chromedriver.exe")

# Растянуть на всю ширину экрана (под разрешение экрана)
driver.maximize_window()
print(driver.get_window_size())

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?15377025964407")

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

driver.find_element_by_id("RESULT_FileUpload-10").send_keys("D://20190914_145745.jpg")