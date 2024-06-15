from playwright.sync_api import Page, Locator
import locators


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def find_element(self, locator: str, element: Locator = None):
        if element:
            return element.locator(locator)
        else:
            return self.page.locator(locator)

    def get_page_title(self):
        return self.page.title()

    def get_current_url(self):
        return self.page.url

    def get_page_footer(self, locator=locators.MainPageLocators.FOOTER):
        return self.find_element(locator)


class MainPage(BasePage):

    url = 'https://demoqa.com/'

    def go_to_main_page(self):
        self.page.goto(self.url)

    def get_banner(self):
        return self.find_element(locator=locators.MainPageLocators.BANNER)

    def find_banner_link(self, element, locator=locators.MainPageLocators.LINK):
        return self.find_element(locator=locator, element=element)

    def get_list_of_cards(self):
        return self.page.locator(locators.MainPageLocators.CARD_ITEM).element_handles()


class ElementsPage(BasePage):

    url = 'https://demoqa.com/elements'

    def go_to_elements_page(self):
        self.page.goto(self.url)

    def get_elements_list(self):
        element = self.find_element(locator=locators.ElementsPage.ELEMENTS_LIST).first
        element = self.find_element(element=element, locator=locators.ElementsPage.SUB_ELEMENTS_LIST)
        elements = self.find_element(element=element, locator=locators.ElementsPage.SUB_ELEMENTS_ITEM).element_handles()
        return elements
