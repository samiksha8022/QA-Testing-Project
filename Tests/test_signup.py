from Pages.signup_page import SignupPage
from utils.test_data import BASE_URL, SIGNUP_DATA
from utils.helpers import handle_alert
from playwright.sync_api import Page


def test_signup(page: Page):

    signup = SignupPage(page)

    # Open website
    page.goto(BASE_URL)

    # Handle alert popup
    page.on("dialog", handle_alert)

    # Open signup form
    signup.open_signup()

    # Enter username
    signup.enter_username(SIGNUP_DATA["username"])

    # Enter password
    signup.enter_password(SIGNUP_DATA["password"])

    # Click signup button
    signup.click_signup()

    # Wait for alert response
    page.wait_for_timeout(2000)

    print("Signup test executed successfully 🚀")
    
    

 
  