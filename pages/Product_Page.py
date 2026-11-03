from pages.Base_page import  BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Product(BasePage):
    Product_xpath=(By.XPATH,"//img[@alt='Sauce Labs Backpack']")
    AddToCart_btn_id=(By.ID,"add-to-cart")
    removeBtn_id=(By.ID,"remove")
    backBtn_id=(By.ID,"back-to-products")
    filterBtn_xpath=(By.XPATH,"//select[@aria-label='Sort products']")
    quantity_xpath=(By.XPATH,"//span[@class='shopping_cart_badge']")

    def __init__(self, driver):
        super().__init__(driver)

    def Check_dtls(self):
        c=self.find_element(self.Product_xpath)
        c.click()

    def addProduct(self):
        self.click(self.AddToCart_btn_id)
   
    def getproductValue(self):
        pr=self.find_element(self.quantity_xpath)
        return pr.text
    
    def removeProduct(self):
        self.click(self.removeBtn_id)

    def back(self):
        self.click(self.backBtn_id)

    def FilterProduct(self,value):
        f=self.find_element(self.filterBtn_xpath)
        
        fi=Select(f)
        #fi.select_by_value(value)
        fi.select_by_index(value)

