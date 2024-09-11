from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class Page_Inventory():
    def __init__(self, driver):
        self.driver = driver
        self.cart = (By.ID,'shopping_cart_container')
        self.order = (By.CLASS_NAME, 'product_sort_container')
        self.item = (By.CLASS_NAME, 'inventory_item_name')

    def select_element(self, element):
        elements = {'onesie':'add-to-cart-sauce-labs-onesie','fleece':'add-to-cart-sauce-labs-fleece-jacket'}
        self.driver.find_element(By.ID,elements[element]).click()
    
    def go_to_cart(self):
        self.driver.find_element(*self.cart).click()

    def select_order_by_value(self, value):
        Select(self.driver.find_element(*self.order)).select_by_value(value)
    
    def select_order_by_visible_text(self, text):
        Select(self.driver.find_element(*self.order)).select_by_visible_text(text)

    def select_order_by_index(self,index):
        Select(self.driver.find_element(*self.order)).select_by_index(index)
    
    def get_articles_names(self):
        items = self.driver.find_elements(*self.item)
        texts = []
        for item in items:
            texts.append(item.text)
        return texts
        



        #1- Ordene de manera descendente
        #2- Devuelvo todos los textos
        #3- Comparo que este todo ordenado