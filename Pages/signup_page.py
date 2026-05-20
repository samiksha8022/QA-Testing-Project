from utils.base_page import BasePage5
from utils.cart_locators import SignupLocators


class SignupPage(BasePage5):

    def open_signup(self):
        self.click(SignupLocators.SIGNUP_MENU)

    def enter_username(self, username):
        self.fill(SignupLocators.USERNAME, username)

    def enter_password(self, password):
        self.fill(SignupLocators.PASSWORD, password)

    def click_signup(self):
        self.click(SignupLocators.SIGNUP_BTN)


         
        