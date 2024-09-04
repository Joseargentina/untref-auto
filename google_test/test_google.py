import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Test_Google(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(8)
        self.driver.get('http://www.google.com')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
    
    def search(self,termino):
        self.driver.find_element(By.ID, 'APjFqb').send_keys(termino+Keys.ENTER)

    def test_hola(self):
        self.search('Hola')
        #titulo = self.driver.find_element(By.CLASS_NAME, 'VuuXrf').text
        #self.assertEqual(titulo,'¡HOLA!')
        self.assertEqual(self.driver.find_element(By.CLASS_NAME, 'VuuXrf').text,'¡HOLA!')

    def test_algo(self):
        self.search('algo')
        diccionario = self.driver.find_element(By.CLASS_NAME, 'gJBeNe.d2F2Td').text
        self.assertEqual(diccionario,'Diccionario')
        
    def test_calculadora(self):
        self.search('calculadora')
        valor = self.driver.find_element(By.CLASS_NAME, 'qv3Wpe').text
        self.assertEqual(valor,'0')
        
if __name__ == '__main__':
    unittest.main()