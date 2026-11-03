from pages.Base_page import  BasePage
from selenium.webdriver.common.by import By

class Checkout(BasePage):
    checkoutBtn_id=(By.ID,"checkout")
    firstName_id=(By.ID,"first-name")
    LastName_id=(By.ID,"last-name")
    ZipCode_id=(By.ID,"postal-code")
    Continue_id=(By.ID,"continue")
    Item_xpath=(By.XPATH,"//div[@class='cart_quantity']")
    FinishBtn_id=(By.ID,"finish")

    def __init__(self, driver):
        super().__init__(driver)

    def checkout(self):
        c=self.find_element(self.checkoutBtn_id)
        c.click()

    def AddInfo(self,firstName,lastName,zipCode):
        self.enter_text(self.firstName_id,firstName)
        self.enter_text(self.LastName_id,lastName)
        self.enter_text(self.ZipCode_id,zipCode)
        self.click(self.Continue_id)

    def getItems(self):
        items=self.find_element(self.Item_xpath)
        return items.text

    def FinishCheckout(self):
        f=self.find_element(self.FinishBtn_id)
        f.click()
    