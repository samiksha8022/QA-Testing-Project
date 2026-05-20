from utils.base_page import BasePage3
from utils.cart_locators import HomePageLocators


class HomePage(BasePage3):

    def __init__(self, page):

        super().__init__(page)

    def open_home_page(self, url):

        self.open_url(url)

    def click_home(self):

        self.click_element(
            HomePageLocators.HOME_MENU
        )

    def click_next_banner(self):

        self.click_element(
            HomePageLocators.NEXT_BANNER
        )

    def click_prev_banner(self):

        self.click_element(
            HomePageLocators.PREV_BANNER
        )

    def open_phones_category(self):

        self.click_element(
            HomePageLocators.PHONES
        )

    def open_laptops_category(self):

        self.click_element(
            HomePageLocators.LAPTOPS
        )

    def open_monitors_category(self):

        self.click_element(
            HomePageLocators.MONITORS
        )

    def open_product(self, product_name):

        self.page.click(
            f"text='{product_name}'"
        )

    def click_next_product(self):

        self.click_element(
            HomePageLocators.NEXT_PRODUCT
        )

    def click_prev_product(self):

        self.click_element(
            HomePageLocators.PREV_PRODUCT
        )

    def verify_footer(self):

        assert self.page.locator(
            HomePageLocators.ABOUT_US
        ).is_visible()

        assert self.page.locator(
            HomePageLocators.GET_IN_TOUCH
        ).is_visible()

        assert self.page.locator(
            HomePageLocators.ADDRESS
        ).is_visible()

        assert self.page.locator(
            HomePageLocators.PHONE
        ).is_visible()

        assert self.page.locator(
            HomePageLocators.EMAIL
        ).is_visible()