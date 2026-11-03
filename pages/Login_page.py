from pages.Base_page import  BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    Username=(By.ID,"user-name")
    Password=(By.ID,"password")
    Login_btn=(By.ID,"login-button")
    Error=(By.XPATH,"//h3[@role='alert']")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, usernamme,password):
        self.enter_text(self.Username,usernamme)
        self.enter_text(self.Password,password)
        self.click(self.Login_btn)

    def getError(self):
        return self.find_element(self.Error).text

    