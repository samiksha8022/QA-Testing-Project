from utils.base_page import BasePage
from utils.cart_locators import CartLocators


class CartPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    # Open cart
    def open_cart(self):
        self.click_element(CartLocators.CART_MENU)

    # Click Place Order button
    def click_place_order(self):
        self.click_element(CartLocators.PLACE_ORDER_BTN)

    # Enter Name
    def enter_name(self, name):
        self.fill_input(CartLocators.NAME_INPUT, name)

    # Enter Country
    def enter_country(self, country):
        self.fill_input(CartLocators.COUNTRY_INPUT, country)

    # Enter City
    def enter_city(self, city):
        self.fill_input(CartLocators.CITY_INPUT, city)

    # Enter Credit Card
    def enter_card(self, card):
        self.fill_input(CartLocators.CREDIT_CARD_INPUT, card)

    # Enter Month
    def enter_month(self, month):
        self.fill_input(CartLocators.MONTH_INPUT, month)

    # Enter Year
    def enter_year(self, year):
        self.fill_input(CartLocators.YEAR_INPUT, year)

    # Click Purchase
    def click_purchase(self):
        self.click_element(CartLocators.PURCHASE_BTN)

    # Click OK button
    def click_ok_btn(self):
        self.click_element(CartLocators.OK_BTN)

    # Delete Product
    def delete_product(self):
        self.click_element(CartLocators.DELETE_BTN)

    # Verify product visible in cart
    def verify_product_in_cart(self, product_name):
        return self.is_visible(f"text='{product_name}'")

    # Get success message title
    def get_success_message(self):
        return self.get_text(".sweet-alert > h2")

    # Get order details
    def get_order_details(self):
        return self.get_text(".sweet-alert > p")

    # Take screenshot
    def capture_screenshot(self, name):
        self.take_screenshot(name)

