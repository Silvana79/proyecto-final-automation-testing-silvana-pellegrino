
import logging

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

from utils.data_reader import get_user, load_products


logger = logging.getLogger(__name__)


def test_login_exitoso(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    user = get_user("valid_user")

    login_page.open()
    login_page.login(user["username"], user["password"])

    inventory_page.wait_until_loaded()

    assert "/inventory.html" in driver.current_url
    assert inventory_page.get_page_title() == "Products"

    logger.info("Login exitoso.")


def test_login_con_credenciales_invalidas(driver):
    login_page = LoginPage(driver)

    user = get_user("invalid_user")

    login_page.open()
    login_page.login(user["username"], user["password"])

    error_message = login_page.get_error_message()

    assert error_message == (
        "Epic sadface: Username and password do not match "
        "any user in this service"
    )

    logger.info("Credenciales inválidas rechazadas correctamente.")


def test_login_usuario_bloqueado(driver):
    login_page = LoginPage(driver)

    user = get_user("locked_user")

    login_page.open()
    login_page.login(user["username"], user["password"])

    error_message = login_page.get_error_message()

    assert error_message == (
        "Epic sadface: Sorry, this user has been locked out."
    )

    logger.info("Usuario bloqueado correctamente identificado.")


def test_catalogo_inventario(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    user = get_user("valid_user")
    expected_products = load_products()

    login_page.open()
    login_page.login(user["username"], user["password"])

    inventory_page.wait_until_loaded()

    assert inventory_page.get_page_title() == "Products"

    product_name, product_price = inventory_page.get_first_product()

    assert product_name.strip() != ""
    assert product_price.startswith("$")

    # Comparamos el primer producto del sitio
    # con el primer registro del archivo CSV.
    assert product_name == expected_products[0]["name"]
    assert product_price == expected_products[0]["price"]

    logger.info(
        "Producto validado: %s | Precio: %s",
        product_name,
        product_price
    )


def test_carrito_primer_producto(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    user = get_user("valid_user")

    login_page.open()
    login_page.login(user["username"], user["password"])

    inventory_page.wait_until_loaded()

    product_name, product_price = inventory_page.get_first_product()

    inventory_page.add_first_product_to_cart()

    assert inventory_page.get_cart_quantity() == "1"

    inventory_page.open_cart()
    cart_page.wait_until_loaded()

    assert "/cart.html" in driver.current_url
    assert cart_page.get_page_title() == "Your Cart"
    assert cart_page.get_products_count() == 1
    assert cart_page.get_first_product_name() == product_name
    assert cart_page.get_first_product_price() == product_price

    logger.info("Producto agregado y verificado en el carrito.")
