from selenium import webdriver
from selenium.webdriver.support.ui import Select

# Chrome
driver = webdriver.Chrome(executable_path = "C:/Users/latar/chromedriver/chromedriver.exe")

# Растянуть на всю ширину экрана (под разрешение экрана)
driver.maximize_window()
print(driver.get_window_size())

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?15377025964407")

element = driver.find_element_by_id("RESULT_RadioButton-9")
drp = Select(element)

# Выбор из видимого текста
# drp.select_by_visible_text('Morning')

# Выбор по индексу
drp.select_by_index(2)

# Выбор по значению
# drp.select_by_value("Radio-2")

# Показать длинну выпадающего списка
print(len(drp.options))

# Показать все значения списка
all_options = drp.options

for option in all_options:
    print(option.text)