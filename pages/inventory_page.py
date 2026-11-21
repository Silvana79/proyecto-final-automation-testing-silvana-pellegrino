
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class InventoryPage:
    PAGE_TITLE = (By.CLASS_NAME, "title")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn_inventory")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

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

    def get_first_product(self):
        first_product = self.wait.until(
            EC.visibility_of_element_located(self.INVENTORY_ITEMS)
        )

        name = first_product.find_element(
            *self.PRODUCT_NAME
        ).text

        price = first_product.find_element(
            *self.PRODUCT_PRICE
        ).text

        return name, price

    def add_first_product_to_cart(self):
        first_product = self.wait.until(
            EC.visibility_of_element_located(self.INVENTORY_ITEMS)
        )

        button = first_product.find_element(
            *self.ADD_TO_CART_BUTTON
        )

        button.click()

        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.CART_BADGE)
        )

    def get_cart_quantity(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.CART_BADGE)
        ).text

    
    def open_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CART_LINK)
        ).click()

        self.wait.until(
            EC.url_contains("/cart.html")
        )