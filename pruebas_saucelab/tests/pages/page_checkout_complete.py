from selenium.webdriver.common.by import By
import re

class Page_Checkout():
    def __init__(self,driver) -> None:
        self.driver = driver
        self.first_name = (By.ID, 'first-name')
        self.last_name = (By.ID, 'last-name')
        self.postal_code = (By.ID, 'postal-code')
        self.continue_button = (By.ID, 'continue')
        self.inventory_item = (By.CLASS_NAME, 'inventory_item_name')
        self.payment_info = (By.CLASS_NAME, 'summary_value_label')
        self.item_total = (By.XPATH, "//div[@class='summary_subtotal_label']")
        self.item_tax = (By.XPATH, "//div[@class='summary_tax_label']")
        self.price_finaly = (By.XPATH, "//div[@class='summary_total_label']")
        self.message_error = (By.XPATH, "//div[@class='error-message-container error']/h3")
        
    def rellenar_form(self,first_name,last_name,postal_code):
        self.driver.find_element(*self.first_name).send_keys(first_name)
        self.driver.find_element(*self.last_name).send_keys(last_name)
        self.driver.find_element(*self.postal_code).send_keys(postal_code)
        
    def verify_element(self,i):
        return self.driver.find_elements(*self.inventory_item)[i].text
        
    def get_payment_info(self):
        return self.driver.find_element(*self.payment_info).text
    
    def get_item_total(self):
        element = self.driver.find_element(*self.item_total)
        text = element.text
        match = re.search(r'Item total:\s*\$([0-9,.]+)', text)
        if match:
            return float(match.group(1))  # Devuelve el valor como float
        else:
            raise ValueError("Item total no encontrado en el texto.")
    
    def get_item_tax(self):
        element = self.driver.find_element(*self.item_tax)
        text = element.text
        match = re.search(r'Tax:\s*\$([0-9,.]+)', text)
        if match:
            return float(match.group(1))  # Devuelve el valor como float
        else:
            raise ValueError("Tax no encontrado en el texto.")
    
    def get_price_finaly(self):
        element = self.driver.find_element(*self.price_finaly)
        text = element.text
        match = re.search(r'Total:\s*\$([0-9,.]+)', text)
        if match:
            return float(match.group(1))  # Devuelve el valor como float
        else:
            raise ValueError("Total no encontrado en el texto.")
        
    def get_message_error(self):
        return self.driver.find_element(*self.message_error).text
    
    def go_to_continue(self):
        return self.driver.find_element(*self.continue_button).click()