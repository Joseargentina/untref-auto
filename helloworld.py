from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()
driver.implicitly_wait(5)
driver.get('http://www.google.com')
driver.find_element(By.ID,'APjFqb').send_keys('Hola'+Keys.ENTER)
driver.find_element(By.LINK_TEXT, "Actualidad").click()
#driver.close()