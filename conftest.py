from selenium import webdriver
import pytest
from pages.Login_page import LoginPage
from pages.Cart_Page import AddToCart

@pytest.fixture()

def setup(browser):

     if browser == 'firefox':
        # Configure Firefox Options to disable password saving prompts
        firefox_options = webdriver.FirefoxOptions()
        
        # Set preferences to block password manager and autofill prompts
        firefox_options.set_preference("signon.rememberSignons", False)
        firefox_options.set_preference("signon.autofillForms", False)
        firefox_options.set_preference("signon.generation.enabled", False)
        firefox_options.set_preference("signon.management.page.fileImport.enabled", False)
        firefox_options.binary_location = r"C:\Program Files\Mozilla Firefox"

        driver = webdriver.Firefox(options=firefox_options)
        
     elif browser == 'edge':
        # Configure Edge Options to disable password saving prompts
        edge_options = webdriver.EdgeOptions()
        
        # Experimental preferences to disable Edge credentials service
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False
        }
        edge_options.add_experimental_option("prefs", prefs)
        
        # Disable leak detection feature flag
        edge_options.add_argument("--disable-features=PasswordLeakDetection")
        
        driver = webdriver.Edge(options=edge_options)
        
     else:
        # Fallback or default browser configuration if none matches
        driver = webdriver.Firefox()
    
     yield driver

     driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browse")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browse")

@pytest.fixture()
def logged_in(setup):

    login=LoginPage(setup)
    login.open("https://www.saucedemo.com/")
    login.login("standard_user","secret_sauce")

    assert "inventory" in setup.current_url.lower(), "login Failed"
    
    return setup

@pytest.fixture()

def cartproductadded(logged_in):
     cart = AddToCart(logged_in)
     cart.AddProduct()
     cart.OpenCart()
     return logged_in 
