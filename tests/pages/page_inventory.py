from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException

class Page_Inventory():
    def __init__(self, driver):
        self.driver = driver  # El driver de Selenium se pasa cuando se crea la instancia de la clase.
        self.cart = (By.ID, 'shopping_cart_container')  # Localizador del carrito de compras, almacenado como una tupla.
        self.order = (By.CLASS_NAME, 'product_sort_container')
        self.item = (By.CLASS_NAME, 'inventory_item_name ')
        self.item_price = (By.CLASS_NAME, 'inventory_item_price')
        self.menu_button = (By.ID,'react-burger-menu-btn')
        self.logout_btn = (By.ID, 'logout_sidebar_link')
        self.wait = WebDriverWait(self.driver, 10)

    def select_element(self, element):
        #pre_element = 'add-to-cart-'+element.replace(' ','-').lower()
        self.driver.find_element(By.ID,'add-to-cart-sauce-labs-'+ element.replace(' ', '-').lower()).click()
    
    def go_to_cart(self):
        # Usa el localizador 'self.cart' para hacer clic en el botón del carrito.
        self.driver.find_element(*self.cart).click()
    
    def select_order_by_value(self,value):
        Select(self.driver.find_element(*self.order)).select_by_value(value)
        
    def select_order_by_index(self,index):
        Select(self.driver.find_element(*self.order)).select_by_index(index)
    
    def select_order_by_visible_text(self,text):
        Select(self.driver.find_element(*self.order)).select_by_visible_text(text)
    
    def get_articles_names(self):
        items = self.driver.find_elements(*self.item)
        articles_text = [] 
        for item in items:
            articles_text.append(item.text)
        return articles_text
    
    def get_prices_names(self):
        items = self.driver.find_elements(*self.item_price)
        prices = []
        for item in items:
            price_text = item.text
            # Limpia los símbolos '$' y convierte los precios a float
            price = float(price_text.replace('$', ''))
            prices.append(price)
        return prices
        
    def logout(self):
        # self.driver.find_element(*self.menu_button).click()
        # self.driver.find_element(*self.logout_btn).click()
        try:
            self.wait.until(EC.element_to_be_clickable(self.menu_button)).click()
            # Wait for the logout button to be visible and clickable
            logout_button = self.wait.until(EC.element_to_be_clickable(self.logout_btn))
            logout_button.click()
        except (NoSuchElementException, ElementNotInteractableException) as e:
            print(f"Error during logout: {e}")
        




        #1- Ordene de manera descendente
        #2- Devuelvo todos los textos
        #3- Comparo que este todo ordenado