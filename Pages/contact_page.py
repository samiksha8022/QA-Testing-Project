from utils.base_page import BasePage2
from utils.cart_locators import ContactLocators


class Contact(BasePage2):

    def __init__(self, page):

        super().__init__(page)

    def open_contact_popup(self):

        self.click_element(ContactLocators.CONTACT_MENU)

    def enter_contact_email(self, email):

        self.fill_input(ContactLocators.CONTACT_EMAIL, email)

    def enter_contact_name(self, name):

        self.fill_input(ContactLocators.CONTACT_NAME, name)

    def enter_message(self, msg):

        self.fill_input(ContactLocators.MESSAGE_BOX, msg)

    def click_send_msg_btn(self):

        self.click_element(ContactLocators.SEND_MESSAGE_BTN)


        