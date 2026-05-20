from playwright.sync_api import expect

from Pages.cart_page import CartPage
from Pages.home_page import HomePage

from utils.test_data import VALID_ORDER_DATA
from utils.test_data import INVALID_ORDER_DATA


# ===============================
# VALID PLACE ORDER TEST
# ===============================

def test_add_to_cart(page):

    home = HomePage(page)
    cart = CartPage(page)

    # Open Website
    home.open_home_page("https://www.demoblaze.com/index.html")

    # Open Product
    home.open_product("Samsung galaxy s6")

    page.wait_for_timeout(2000)

    # Handle Alert
    page.once("dialog", lambda dialog: dialog.accept())

    # Add to cart
    page.click("a:has-text('Add to cart')")

    page.wait_for_timeout(5000)

    # Open cart
    cart.open_cart()
    page.wait_for_timeout(3000)

    # Verify product
    expect(
        page.get_by_text("Samsung galaxy s6")
    ).to_be_visible()

    # Place order
    cart.click_place_order()

    # Fill valid data
    cart.enter_name(VALID_ORDER_DATA["name"])

    cart.enter_country(VALID_ORDER_DATA["country"])

    cart.enter_city(VALID_ORDER_DATA["city"])

    cart.enter_card(VALID_ORDER_DATA["card"])

    cart.enter_month(VALID_ORDER_DATA["month"])

    cart.enter_year(VALID_ORDER_DATA["year"])

    # Purchase
    cart.click_purchase()

    page.wait_for_timeout(3000)

    # Get Success Message
    success_msg = cart.get_success_message()

    print(success_msg)

    # Validation
    expect(
        page.locator(".sweet-alert > h2")
    ).to_have_text("Thank you for your purchase!")

    # Screenshot
    cart.capture_screenshot("valid_order")

    # Click OK
    cart.click_ok_btn()


# ===============================
# INVALID PLACE ORDER TEST
# ===============================

def test_place_order_invalid(page):

    home = HomePage(page)
    cart = CartPage(page)

    # Open Website
    home.open_home_page("https://www.demoblaze.com/index.html")

    # Open Cart
    cart.open_cart()

    # Click Place Order
    cart.click_place_order()

    # Fill Invalid Data
    cart.enter_name(INVALID_ORDER_DATA["name"])

    cart.enter_country(INVALID_ORDER_DATA["country"])

    cart.enter_city(INVALID_ORDER_DATA["city"])

    cart.enter_card(INVALID_ORDER_DATA["card"])

    cart.enter_month(INVALID_ORDER_DATA["month"])

    cart.enter_year(INVALID_ORDER_DATA["year"])

    # Purchase
    cart.click_purchase()

    page.wait_for_timeout(3000)

    # Screenshot
    cart.capture_screenshot("invalid_order")

    # Validation
    expect(
        page.locator("text=Thank you for your purchase")
    ).to_be_visible()


# ===============================
# DELETE PRODUCT TEST
# ===============================

def test_delete_cart_product(page):

    home = HomePage(page)
    cart = CartPage(page)

    # Open Website
    home.open_home_page("https://www.demoblaze.com/index.html")

    # Open Product
    home.open_product("Samsung galaxy s6")

    # Handle Alert
    page.once("dialog", lambda dialog: dialog.accept())

    # Add To Cart
    page.click("a:has-text('Add to cart')")

    page.wait_for_timeout(3000)

    # Open Cart
    cart.open_cart()

    page.wait_for_timeout(2000)

    # Delete Product
    cart.delete_product()

    page.wait_for_timeout(3000)

    # Screenshot
    cart.capture_screenshot("delete_product")

