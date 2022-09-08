from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\\Users\\Eira Medina\\Documents\\automation-python\\drivers\\chromedriver.exe')
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.google.com.mx/?hl=es-419")
driver.find_element_by_name("q").send_keys("python")
driver.find_element_by_name("btnK").click()
driver.close()
driver.quit()
print("Test complete PASS")
