from Pages.login_page import LoginPage

from utils.test_data import (
    BASE_URL,
    VALID_LOGIN_DATA,
    INVALID_LOGIN_DATA
)

from playwright.sync_api import (
    Page,
    expect
)


# ==========================
# VALID LOGIN TEST
# ==========================

def test_valid_login(page: Page):

    login = LoginPage(page)

    # Open Website
    page.goto(BASE_URL)


    # Handle Alert
    def handle_alert(dialog):

        print(
            "Login Alert Message:",
            dialog.message
        )

        dialog.accept()

    page.on("dialog", handle_alert)



    # Open Login Popup
    login.open_login_popup()

    # Enter Valid Data
    login.enter_username(
        VALID_LOGIN_DATA["username"]
    )

    login.enter_password(
        VALID_LOGIN_DATA["password"]
    )

    # Click Login
    login.click_login()
    print("User text:", page.locator("#nameofuser").text_content())


    # Verify User Logged In
    expect(
        page.locator("#nameofuser")
    ).to_be_visible(timeout=2000)

    print("Valid Login Successful")


# ==========================
# INVALID LOGIN TEST
# ==========================

def test_invalid_login(page: Page):

    login = LoginPage(page)

    # Open Website
    page.goto(BASE_URL)

    # Handle Alert
    def handle_alert(dialog):

        print(
            "Invalid Login Message :",
            dialog.message
        )

        # Verify Alert Message
        assert dialog.message == "Wrong password."

        dialog.accept()

    page.on("dialog", handle_alert)

    # Open Login Popup
    login.open_login_popup()

    # Enter Invalid Data
    login.enter_username(
        INVALID_LOGIN_DATA["username"]
    )

    login.enter_password(
        INVALID_LOGIN_DATA["password"]
    )

    # Click Login
    login.click_login()

    page.wait_for_timeout(3000)





def test_logout(page):

    # assume already logged in

    page.click("#logout2")

    # verify logout success via UI changes

    expect(page.locator("#login2")).to_be_visible()      # Login button visible
    expect(page.locator("#logout2")).to_be_hidden()      # Logout hidden
    expect(page.locator("#nameofuser")).to_be_hidden()   # Username hidden