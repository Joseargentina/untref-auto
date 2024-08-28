from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://untref.edu.ar/')
driver.find_element(By.CLASS_NAME, 'btn-search').click()
driver.find_element(By.NAME, 'q').send_keys('Diplomatura')
driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div[1]/div/nav/ul/li/div/form/input[3]').click()
driver.find_element(By.XPATH,'/html/body/div[1]/section/section/div[2]/div/div[1]/a').click()



#/html/body/div[1]/section/section/div[2]/div/div[1]/a