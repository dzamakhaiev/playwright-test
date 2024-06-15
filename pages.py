from playwright.sync_api import Page
import locators


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def find_element(self, locator: str):
        return self.page.locator(locator)

    def get_title(self):
        return self.page.title()


class MainPage(BasePage):

    url = 'https://demoqa.com/'

    def go_to_main_page(self):
        self.page.goto(self.url)

    def get_footer(self, locator=locators.MainPageLocators.FOOTER):
        return self.find_element(locator)
