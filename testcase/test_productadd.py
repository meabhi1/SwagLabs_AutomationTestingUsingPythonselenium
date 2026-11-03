
from pages.Cart_Page import AddToCart
from logs.customeLogger import LoggGen
import os


class TestCart:

    def test_AddCart(self, logged_in):

        logger = LoggGen.Logger()

        cart = AddToCart(logged_in)

        try:
            logger.info("-- Login successful")
            logger.info("-- Started Add to Cart test")

            # Add product to cart
            cart.AddProduct()

            logger.info("-- Product clicked successfully")

            # Verify cart count
            count = cart.getCart()

            logger.info(f"-- Cart count is: {count}")

            assert count == "1", "Product not added to cart"

            logger.info("-- Product added to cart successfully")

            # Open cart page
            cart.OpenCart()

            logger.info("-- Opened cart page")

            # Verify cart page
            assert "cart" in logged_in.current_url, \
                "Cart page not opened"

            logger.info("-- Cart page opened successfully")
            logger.info("-- Add to Cart test passed")

        except AssertionError:
            logger.error("-- Add to Cart test failed")

            # Create Screenshot folder
            folder = os.path.join(
                os.getcwd(), "Screenshots", "Cart"
            )

            os.makedirs(folder, exist_ok=True)

            # Capture screenshot
            screenshot_path = os.path.join(
                folder, "Add_to_Cart_failed.png"
            )

            logged_in.save_screenshot(screenshot_path)

            logger.info(f"-- Screenshot saved at: {screenshot_path}")

            raise
