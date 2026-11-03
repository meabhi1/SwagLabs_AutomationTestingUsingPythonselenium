from pages.Base_page import  BasePage
from selenium.webdriver.common.by import By

class AddToCart(BasePage):
    Add_To_Cart_id=(By.ID,"add-to-cart-sauce-labs-backpack")
    Cart_btn_xpath=(By.XPATH,"//a[@aria-label='Cart, 1 items']")
    CartCount_xpath=(By.XPATH,"//span[@class='shopping_cart_badge']")

    def __init__(self, driver):
        super().__init__(driver)

    def AddProduct(self):
        a=self.find_element(self.Add_To_Cart_id)
        a.click()

    def OpenCart(self):
        s=self.find_element(self.Cart_btn_xpath)
        s.click()

    def getCart(self):
        g=self.find_element(self.CartCount_xpath)
        return g.text
    