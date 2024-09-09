import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.page_login import Page_Login
from pages.page_inventory import Page_Inventory
from pages.page_cart import Page_Cart
from pages.page_checkout import Page_Checkout
from pages.page_checkout_II import Page_Checkout_II
class Test1(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get('https://www.saucedemo.com/')

    def tearDown(self) -> None:
        self.driver.close()
        self.driver.quit()

    def finish(self):
        self.driver.find_element(By.ID,'finish').click()

    def get_final_message(self):
        return self.driver.find_element(By.CLASS_NAME,'complete-header').text

    def test_caso1(self):
        page_login = Page_Login(self.driver)
        page_login.login('standard_user','secret_sauce')
        page_inventory = Page_Inventory(self.driver)
        page_inventory.select_element('onesie')
        page_inventory.select_element('fleece')
        page_inventory.go_to_cart()
        page_cart = Page_Cart(self.driver)
        page_cart.go_to_checkout()
        page_checkout = Page_Checkout(self.driver)
        page_checkout.checkout('pepe','pepe','1111')
        page_checkout_II = Page_Checkout_II(self.driver)
        article = page_checkout_II.verify_element(0)
        self.assertEqual('Sauce Labs Onesie', article)
        article = page_checkout_II.verify_element(1)
        self.assertEqual('Sauce Labs Fleece Jacket', article)
        self.finish()
        message = self.get_final_message()
        self.assertEqual('Thank you for your order!', message)