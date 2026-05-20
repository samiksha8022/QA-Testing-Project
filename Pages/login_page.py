from utils.base_page import BasePage4

from utils.cart_locators import LoginPageLocators


class LoginPage(BasePage4):

    def __init__(self, page):

        super().__init__(page)

    def open_login_popup(self):

        self.click_element(
            LoginPageLocators.LOGIN_MENU
        )

    def enter_username(self, user):

        self.fill_text(
            LoginPageLocators.USERNAME,
            user
        )

    def enter_password(self, pwd):

        self.fill_text(
            LoginPageLocators.PASSWORD,
            pwd
        )

    def click_login(self):

        self.click_element(
            LoginPageLocators.LOGIN_BUTTON
        )