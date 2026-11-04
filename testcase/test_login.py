
from pages.Login_page import LoginPage
from logs.customeLogger import LoggGen

import os
import pytest
import openpyxl
import yaml

class TestLogin:

    base_Url = "https://www.saucedemo.com/"
    #username = "standard_user"  # Incorrect username to test failure
    #password = "secret_sauce"

#    @pytest.mark.parametrize(
#    "username,password,expected",
#    [
#        ("standard_user", "secret_sauce", True),
#        ("standard_user", "wrong_password", False),
#        ("", "secret_sauce", False),
#        ("locked_out_user", "secret_sauce", False)
#    ]
#)
    #def getExcelData(file_path,sheetname):
    #    workbook=openpyxl.load_workbook(file_path)
    #    sheeet=workbook[sheetname]
    #    data=[]
#
    #    for row in sheeet.iter_rows(min_row=2,values_only=True):
    #        data.append(row)
    #    return data
    #
    #testdata=getExcelData("test_data.xlsx","login_test")
    def getyamldta(file_path):
        with open(file_path,"r",encoding="utf-8")as f:
            return yaml.safe_load(f)
        
    yaml_data=getyamldta("test_yaml.yaml")

    testParams=[(item["username"],item["password"],item["expected"]) for item in yaml_data]

   ## @pytest.mark.parametrize("username,password",testdata)
    @pytest.mark.parametrize("username,password,expected",testParams)
    def test_login(self, setup,username,password,expected):

        lo = LoginPage(setup)
        logger = LoggGen.Logger()

        logger.info("-- Opened site successfully")
        lo.open(self.base_Url)

        try:
            logger.info("-- Started login")

            lo.login(username, password)

            assert "inventory" in setup.current_url, \
                "Login failed: Inventory page not opened"

            logger.info("-- Logged in successfully")

            
        except AssertionError:
            
            assert lo.getError() != ""
            logger.error("-- Login failed")

            folder = os.path.join(
                os.getcwd(), "Screenshots","Login"
            )

            os.makedirs(folder, exist_ok=True)

            screenshot_path = os.path.join(
                folder, "login_Failed.png"
            )

            setup.save_screenshot(screenshot_path)

            logger.info(f"-- Screenshot saved: {screenshot_path}")

            raise
