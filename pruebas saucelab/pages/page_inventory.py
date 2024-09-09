from selenium.webdriver.common.by import By

class Page_Inventory():
    def __init__(self, driver):
        self.driver = driver
        self.cart = (By.ID,'shopping_cart_container')

    def select_element(self, element):
        elements = {'onesie':'add-to-cart-sauce-labs-onesie','fleece':'add-to-cart-sauce-labs-fleece-jacket'}
        self.driver.find_element(By.ID,elements[element]).click()
    
    def go_to_cart(self):
        self.driver.find_element(*self.cart).click()