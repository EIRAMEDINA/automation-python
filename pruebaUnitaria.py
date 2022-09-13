from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest
import HtmlTestRunner


class GoogleSearch(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='C:\\Users\\Eira Medina\\Documents\\automation-python\\drivers\\chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    
    
    def test_search_automation(self):
        self.driver.get('https://www.google.com.mx/?hl=es-419')
        self.driver.find_element(By.NAME, "q").send_keys('python')
        self.driver.find_element(By.NAME, "btnK").click()
        time.sleep(1000)

                
    def test_searhc_name(self):
        self.driver.get('https://www.google.com.mx/?hl=es-419')
        self.driver.find_element(By.NAME, "q").send_keys('selenium')
        self.driver.find_element(By.NAME, "btnK").click()
        time.sleep(1000)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test complete")
        
        
if __name__ ==  '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Eira Medina\Documents\\automation-python\\reports'))
