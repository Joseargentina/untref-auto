from selenium.webdriver.common.by import By
class Page_Finish():
    def __init__(self,driver):
        self.driver = driver
        self.finish_button = (By.ID, 'finish')
        self.message_final = (By.CLASS_NAME,'complete-header')
    
    def finish(self):
        self.driver.find_element(*self.finish_button).click()
    def get_final_message(self):
        return self.driver.find_element(*self.message_final).text