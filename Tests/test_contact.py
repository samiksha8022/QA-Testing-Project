from Pages.contact_page import Contact
from utils.test_data import CONTACT_DATA
from utils.test_data import INVALID_CONTACT_DATA
from utils.helpers import handle_alert
from playwright.sync_api import Page,expect


def test_contact(page: Page):

    contact = Contact(page)

    # Open Website
    page.goto("https://www.demoblaze.com/index.html")

    # Handle Alert Popup
    page.on("dialog", handle_alert)

    # Open Contact Popup
    contact.open_contact_popup()

    # Fill Contact Form
    contact.enter_contact_email(CONTACT_DATA["email"])

    contact.enter_contact_name(CONTACT_DATA["name"])

    contact.enter_message(CONTACT_DATA["message"])

    # Click Send Message
    contact.click_send_msg_btn()

    # Wait
    page.wait_for_timeout(5000)


def test_contact_invalid_data(page: Page):

    contact = Contact(page)

    # Open Website
    page.goto("https://www.demoblaze.com/index.html")

    # Handle Popup
    page.on("dialog", handle_alert)

    # Open Contact Form
    contact.open_contact_popup()

    # Enter Invalid Data
    contact.enter_contact_email(
        INVALID_CONTACT_DATA["invalid_email"]
    )

    contact.enter_contact_name(
        INVALID_CONTACT_DATA["blank_name"]
    )

    contact.enter_message(
        INVALID_CONTACT_DATA["blank_message"]
    )

    # Click Send
    contact.click_send_msg_btn()
    # expect(page.locator("error_locator")).to_be_visible()

    page.wait_for_timeout(5000)


