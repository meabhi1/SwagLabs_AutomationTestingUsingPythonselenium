from logs.customeLogger import LoggGen
from pages.Checkout_Page import Checkout
import os

class TestCheckout:
    firstname="Abhijeet"
    lastname="Jha"
    zipCode="112233"

    def test_checkout(self,cartproductadded):
        pymntDone=Checkout(cartproductadded)

        logger=LoggGen.Logger()

        try:
            pymntDone.checkout()
            
            pymntDone.AddInfo(self.firstname,self.lastname,self.zipCode)

            items=pymntDone.getItems()

           # 1. Verify that the product is actually in the checkout list (comparing as an integer)
            assert int(items) == 1, f"Expected 1 item in checkout, but found: {items}"

            # 2. Verify that you have successfully navigated to the checkout page URL
            assert "checkout" in cartproductadded.current_url.lower(), f"Not on checkout page. Current URL: {cartproductadded.current_url}"

            pymntDone.FinishCheckout()

            assert "Checkout: Complete!" in cartproductadded.page_source, "payment not done"
        except AssertionError :

            folder=os.path.join("Screenshots","checkout")
            os.makedirs(folder,exist_ok=True)

            cartproductadded.save_screenshot(f"{folder}\\checkout_failure.png")

            raise 
        
            

