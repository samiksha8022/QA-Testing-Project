from Pages.home_page import HomePage
# from utils.base_page import BasePage3

from utils.test_data import (
    BASE_URL,
    PRODUCTS
)

from utils.helpers import print_message

from playwright.sync_api import Page


def test_home_page(page: Page):

    home = HomePage(page)

    # Open Website
    home.open_home_page(BASE_URL)

    # Verify Title
    assert page.title() == "STORE"

    print_message(
        "Home Page Opened Successfully"
    )

    # Banner Actions
    home.click_next_banner()

    home.click_prev_banner()

    page.wait_for_timeout(2000)

    # Phones Category
    home.open_phones_category()

    page.wait_for_timeout(2000)

    # Open Phone Product
    home.open_product(
        PRODUCTS["phone"]
    )

    page.wait_for_timeout(2000)

    page.go_back()

    # Laptops Category
    home.open_laptops_category()

    page.wait_for_timeout(3000)

    # Open Laptop Product
    home.open_product(
        PRODUCTS["laptop"]
    )

    page.go_back()

    # Monitors Category
    home.open_monitors_category()

    page.wait_for_timeout(3000)

    # Product Buttons
    home.click_next_product()

    home.click_prev_product()


def test_footer(page: Page):

    home = HomePage(page)

    # Open Website
    home.open_home_page(BASE_URL)

    # Scroll Footer
    home.scroll_to_bottom()

    # Verify Footer
    home.verify_footer()

    print_message(
        "Footer Verified Successfully"
    )



