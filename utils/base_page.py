class BasePage:

    def __init__(self, page):

        self.page = page

    # ==========================
    # Open URL
    # ==========================
    def open_url(self):

        self.page.goto("https://www.demoblaze.com/index.html")

    # ==========================
    # Click Element
    # ==========================
    def click_element(self, locator):

        self.page.click(locator)

    # ==========================
    # Fill Input Field
    # ==========================
    def fill_input(self, locator, value):

        self.page.fill(locator, value)

    # ==========================
    # Get Text
    # ==========================
    def get_text(self, locator):

        return self.page.locator(locator).text_content()

    # ==========================
    # Check Element Visible
    # ==========================
    def is_visible(self, locator):

        return self.page.locator(locator).is_visible()

    # ==========================
    # Wait
    # ==========================
    def wait(self, time):

        self.page.wait_for_timeout(time)

    # ==========================
    # Screenshot
    # ==========================
    def take_screenshot(self, name):

        self.page.screenshot(
            path=f"screenshots/{name}.png"
        )

    # ==========================
    # Go Back
    # ==========================
    def go_back(self):

        self.page.go_back()

    # ==========================
    # Scroll Bottom
    # ==========================
    def scroll_to_bottom(self):

        self.page.evaluate(
            "window.scrollTo(0, document.body.scrollHeight)"
        )




class BasePage2:

    def __init__(self, page):
        self.page = page

    def click_element(self, locator):
        self.page.click(locator)

    def fill_input(self, locator, value):
        self.page.fill(locator, value)

    def wait(self, time):
        self.page.wait_for_timeout(time)


class BasePage3:

    def __init__(self, page):

        self.page = page

    def open_url(self, url):

        self.page.goto(url)

    def click_element(self, locator):

        self.page.click(locator)

    def fill_text(self, locator, value):

        self.page.fill(locator, value)

    def get_title(self):

        return self.page.title()

    def wait(self, time):

        self.page.wait_for_timeout(time)

    def go_back_page(self):

        self.page.go_back()

    def scroll_to_bottom(self):

        self.page.evaluate(
            "window.scrollTo(0, document.body.scrollHeight)"
        )



class BasePage4:

    def __init__(self, page):

        self.page = page

    def click_element(self, locator):

        self.page.click(locator)

    def fill_text(self, locator, value):

        self.page.fill(locator, value)

    def open_url(self, url):

        self.page.goto(url)

    def wait(self, time):

        self.page.wait_for_timeout(time)





class BasePage5:

    def __init__(self, page):
        self.page = page

    def click(self, locator):
        self.page.click(locator)

    def fill(self, locator, value):
        self.page.fill(locator, value)

    def open(self, url):
        self.page.goto(url)