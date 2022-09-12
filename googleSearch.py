from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='C:\\Users\\Eira Medina\\Documents\\automation-python\\drivers\\chromedriver.exe')
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.google.com.mx/?hl=es-419")
Element = driver.find_element(By.NAME, "q").send_keys('python')
Element = driver.find_element(By.NAME, "btnK").click()
driver.quit()
print("Test complete PASS")