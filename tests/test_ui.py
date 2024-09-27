import unittest
from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
from dotenv import load_dotenv
import os
from selenium.webdriver.chrome.options import Options
from pages.page_login import Page_Login
from pages.page_inventory import Page_Inventory
from pages.page_cart import Page_Cart
from pages.page_checkout_complete import Page_Checkout
from pages.page_finish import Page_Finish

class Compras(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        options = Options()
        options.add_argument('--incognito')
        options.add_argument('--headless')
        # cls.driver = webdriver.Firefox(options=options)
        cls.driver = webdriver.Chrome(options = options)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
    
    def setUp(self) -> None:
        load_dotenv()
        base_url = os.getenv('https://www.saucedemo.com/')
        user = os.getenv('standard_user')
        password = os.getenv('secret_sauce')
        # print(f"Base URL: {base_url}") 
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(os.getenv('https://www.saucedemo.com/'))
        page_login = Page_Login(self.driver)
        page_login.login(user,password)
        self.page_inventory = Page_Inventory(self.driver)

    # def tearDown(self) -> None:
    #     self.page_inventory.logout()
    #     self.driver.close()
    #     self.driver.quit()

    def test_compra_basica(self):
        self.page_inventory.select_element('onesie')
        self.page_inventory.select_element('fleece Jacket')
        self.page_inventory.go_to_cart()
        page_cart = Page_Cart(self.driver)
        page_cart.go_to_checkout()
        page_checkout = Page_Checkout(self.driver)
        page_checkout.rellenar_form('Andres','Zarpilla','6634')
        page_checkout.go_to_continue()
        
        #Verificar los datos del checkout
        self.assertEqual(page_checkout.verify_element(0),'Sauce Labs Onesie')
        self.assertEqual(page_checkout.verify_element(1),'Sauce Labs Fleece Jacket')
        self.assertEqual(page_checkout.get_payment_info(),'SauceCard #31337')
        self.assertEqual(page_checkout.get_item_total(), 57.980000000000004)
        self.assertEqual(page_checkout.get_item_tax(), 4.64)
        self.assertEqual(page_checkout.get_price_finaly(), 62.62)
        
        #Final
        page_finish = Page_Finish(self.driver)
        page_finish.finish()
        self.assertEqual(page_finish.get_final_message(),'Thank you for your order!')
    
    def test_order_by_name_desc(self):
        # self.page_inventory.select_order_by_value('za')
        self.page_inventory.select_order_by_index(1)
        texts = self.page_inventory.get_articles_names()
        self.assertEqual(texts, sorted(texts, reverse=True))

    def test_order_by_name_asc(self):
        # self.page_inventory.select_order_by_value('az')
        self.page_inventory.select_order_by_index(0)
        self.page_inventory.select_order_by_visible_text('Name (A to Z)')
        texts = self.page_inventory.get_articles_names()
        self.assertEqual(texts, sorted(texts))
    
    def test_order_by_price_low_to_hight(self):
        self.page_inventory.select_order_by_value('lohi')
        prices = self.page_inventory.get_prices_names()
        self.assertEqual(prices, sorted(prices))
        
    def test_order_by_price_hight_to_low(self):
        self.page_inventory.select_order_by_visible_text('Price (high to low)')
        prices = self.page_inventory.get_prices_names()
        self.assertEqual(prices, sorted(prices, reverse=True))

    def test_compra_completa(self):
        self.page_inventory.select_element('Backpack')
        self.page_inventory.select_element('Fleece Jacket')
        page_cart = Page_Cart(self.driver)
        page_cart.remove_to_cart('backpack')
        self.page_inventory.select_element('bike-light')
        self.page_inventory.go_to_cart()
        page_cart.remove_to_cart('bike-light')
        page_cart.continue_shopping()
        self.page_inventory.select_element('bolt-t-shirt')
        self.page_inventory.go_to_cart()
        page_cart.go_to_checkout()
        page_checkout = Page_Checkout(self.driver)
        page_checkout.go_to_continue()
        self.assertEqual(page_checkout.get_message_error(),'Error: First Name is required')
        page_checkout.rellenar_form('Andres','Zarpilla','6634')
        page_checkout.go_to_continue()
        
        #Verificar los datos del checkout
        self.assertEqual(page_checkout.verify_element(0),'Sauce Labs Fleece Jacket')
        self.assertEqual(page_checkout.verify_element(1),'Sauce Labs Bolt T-Shirt')
        self.assertEqual(page_checkout.get_payment_info(),'SauceCard #31337')
        self.assertEqual(page_checkout.get_item_total(), 65.98)
        self.assertEqual(page_checkout.get_item_tax(), 5.28)
        self.assertEqual(page_checkout.get_price_finaly(), 71.26)
        
        #Final
        page_finish = Page_Finish(self.driver)
        page_finish.finish()
        self.assertEqual(page_finish.get_final_message(),'Thank you for your order!')
        
if __name__ == '__main__':
    unittest.main()