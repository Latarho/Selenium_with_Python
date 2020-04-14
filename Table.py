from selenium import webdriver

# Chrome
driver = webdriver.Chrome(executable_path = "C:/Users/latar/chromedriver/chromedriver.exe")

driver.get("file:///C:/SeleniumPractice/sample.html")

len(driver.find_element_by_xpath("/html/body/table/tbody/tr"))

rows = len(driver.find_element_by_xpath("/html/body/table/tbody/tr")) # count number of rows
cols = len(driver.find_element_by_xpath("/html/body/table/tbody/tr[1]/th")) # count number of columns

print(rows)
print(cols)

for r in range(2, rows+1):
    for c in range(1, cols+1):
        value = driver.find_element_by_xpath("/html/body/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text()
        print(value, end='      ') # Product 0001 10
    print()