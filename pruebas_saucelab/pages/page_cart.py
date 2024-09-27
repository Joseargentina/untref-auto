from selenium.webdriver.common.by import By

class Page_Cart():
    def __init__(self,driver):
        self.driver = driver
        self.checkout_button = (By.ID, 'checkout')
        self.continue_button = (By.ID, 'continue-shopping')

    def go_to_checkout(self):
        self.driver.find_element(*self.checkout_button).click()
    
    def continue_shopping(self):
        self.driver.find_element(*self.continue_button).click()
        
    def remove_to_cart(self,productId):
        remove_button = (By.ID, f'remove-sauce-labs-{productId}')
        self.driver.find_element(*remove_button).click()