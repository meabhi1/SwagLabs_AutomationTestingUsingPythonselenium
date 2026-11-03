import os
from logs.customeLogger import LoggGen
from pages.Product_Page import Product

class TestProductOpt:
    # Note: Swag Labs values are strings like "za", "az", "lohi", "hilo"
    #values = "za"
    values="2"

    def test_product(self, logged_in):

        logger = LoggGen.Logger()
        logger.info("--- Starting Testcase: test_product ---")
        
        pro = Product(logged_in)

        logger.info("Navigating to product details page.")
        pro.Check_dtls()

        try:
            logger.info("Adding product to cart.")
            pro.addProduct()

            items = pro.getproductValue()
            logger.info(f"Checking shopping cart badge value: {items}")

            assert int(items) == 1, f"Product not Added but found {items}"
            logger.info("Assertion passed: Product added successfully.")

            logger.info("Removing product from cart.")
            pro.removeProduct()

            logger.info("Navigating back to main inventory page.")
            pro.back()

            assert "inventory" in logged_in.current_url, f" Not Moved to inventory than {logged_in.current_url} "
            logger.info("Assertion passed: Successfully returned to inventory page.")

            logger.info(f"Filtering product list by value: {self.values}")
            pro.FilterProduct(self.values)
            logger.info("Filter applied successfully. Test passed.")

        except AssertionError :
            logger.error(f"Assertion failed during test execution")

            folder = os.path.join("Screenshots", "Product")

            os.makedirs(folder, exist_ok=True)

            logged_in.save_screenshot(f"{folder}\\ProductFailed.png")
            logger.error(f"Saved failure screenshot to: {folder}\\ProductFailed.png")

            raise 
