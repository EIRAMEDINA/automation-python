from lib2to3.pgen2.token import NAME
import time
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select




driver = webdriver.Chrome(executable_path='C:\\Users\\Eira Medina\\Documents\\automation-python\\drivers\\chromedriver.exe')
driver.implicitly_wait(10)
driver.maximize_window()
print("obteniendo las coordenadas de la ventana actual: " , driver.get_window_position())

    
driver.get('https://demo.guru99.com/test/newtours/')
print(driver.current_url) 

#registro#

Element = driver.find_element(By.LINK_TEXT, "REGISTER").click()
Element = driver.find_element(By.NAME, "firstName").send_keys('PRUEBA')
Element = driver.find_element(By.NAME, "lastName").send_keys('PYTHON')
Element = driver.find_element(By.NAME , "phone").send_keys('5512345678')
Element = driver.find_element(By.ID , "userName").send_keys('P.PYTHON')
Element = driver.find_element(By.NAME , "address1").send_keys('BENUSIANO CARRANZA')
Element = driver.find_element(By.NAME , "city").send_keys('MÉXICO')
Element = driver.find_element(By.NAME , "state").send_keys('DISTRITO FEDERAL')
Element = driver.find_element(By.NAME , "postalCode").send_keys('01800')

select = Select(driver.find_element(By.NAME, "country"))
select.select_by_visible_text('MEXICO')

    
Element = driver.find_element(By.NAME , "email").send_keys('P.PYTHON@gmail.COM')
Element = driver.find_element(By.NAME , "password").send_keys('123456')
Element = driver.find_element(By.NAME , "confirmPassword").send_keys('123456')
driver.get_screenshot_as_file('C:\\Users\\Eira Medina\\Documents\\automation-python\\Screenshots\\registro_mercuryTours.png')



Element = driver.find_element(By.NAME, "submit").click()