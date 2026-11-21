from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CartPage:
    PAGE_TITLE = (By.CLASS_NAME, "title")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")
    REMOVE_BUTTON = (By.CLASS_NAME, "cart_button")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_until_loaded(self):
        self.wait.until(
            EC.visibility_of_element_located(self.PAGE_TITLE)
        )

    def get_page_title(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.PAGE_TITLE)
        ).text

    def get_first_product_name(self):
        first_item = self.wait.until(
            EC.visibility_of_element_located(self.CART_ITEMS)
        )

        return first_item.find_element(
            *self.PRODUCT_NAME
        ).text

    def get_first_product_price(self):
        first_item = self.wait.until(
            EC.visibility_of_element_located(self.CART_ITEMS)
        )

        return first_item.find_element(
            *self.PRODUCT_PRICE
        ).text

    def get_products_count(self):
        return len(
            self.driver.find_elements(*self.CART_ITEMS)
        )

    def remove_first_product(self):
        first_item = self.wait.until(
            EC.visibility_of_element_located(self.CART_ITEMS)
        )

        first_item.find_element(
            *self.REMOVE_BUTTON
        ).click()
