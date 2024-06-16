from playwright.sync_api import Page, Locator
import locators
from logger import logger


page_logger = logger.Logger('test', level='DEBUG')


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def find_element(self, locator: str, element: Locator = None):
        page_logger.debug(f'Finding locator {locator} for current page or element "{element}".')
        if element:
            return element.locator(locator)
        else:
            return self.page.locator(locator)

    def get_page_title(self):
        page_logger.info('Finding title for current page.')
        return self.page.title()

    def get_current_url(self):
        page_logger.info('Returning url of current page.')
        return self.page.url

    def get_page_footer(self, locator=locators.MainPageLocators.FOOTER):
        page_logger.info('Finding footer for current page.')
        return self.find_element(locator)


class MainPage(BasePage):

    url = 'https://demoqa.com/'

    def go_to_main_page(self):
        page_logger.info('Go to main page.')
        self.page.goto(self.url)

    def get_banner(self):
        page_logger.info('Finding banner element on current page.')
        return self.find_element(locator=locators.MainPageLocators.BANNER)

    def find_banner_link(self, element, locator=locators.MainPageLocators.LINK):
        page_logger.info('Finding link for banner element.')
        return self.find_element(locator=locator, element=element)

    def get_list_of_cards(self):
        page_logger.info('Finding cards list on current page.')
        return self.page.locator(locators.MainPageLocators.CARD_ITEM).element_handles()


class ElementsPage(BasePage):

    url = 'https://demoqa.com/elements'

    def go_to_elements_page(self):
        page_logger.info('Go to elements page.')
        self.page.goto(self.url)

    def get_elements_list(self):
        page_logger.info('Finding elements list on current page.')
        element = self.find_element(locator=locators.ElementsPage.ELEMENTS_LIST).first
        element = self.find_element(element=element, locator=locators.ElementsPage.SUB_ELEMENTS_LIST)
        elements = self.find_element(element=element, locator=locators.ElementsPage.SUB_ELEMENTS_ITEM).element_handles()
        return elements


class TextBoxPage(BasePage):

    url = 'https://demoqa.com/text-box'

    def go_to_text_box_page(self):
        page_logger.info('Go to text box page.')
        self.page.goto(self.url)

    def fill_text_fields(self, field_dict: dict):
        page_logger.info('Filling text form on current page.')
        name_field = self.find_element(locator=locators.TextBoxPage.FULL_NAME)
        email_field = self.find_element(locator=locators.TextBoxPage.EMAIL)
        current_field = self.find_element(locator=locators.TextBoxPage.CURRENT_ADDRESS)
        permanent_field = self.find_element(locator=locators.TextBoxPage.PERMANENT_ADDRESS)

        name_field.type(field_dict.get('full_name', ''))
        email_field.type(field_dict.get('email', ''))
        current_field.type(field_dict.get('current_address', ''))
        permanent_field.type(field_dict.get('permanent_address', ''))

        self.find_element(locator=locators.TextBoxPage.SUBMIT).click()

    def read_output(self):
        page_logger.info('Reading form output of current page.')
        output = self.find_element(locator=locators.TextBoxPage.OUTPUT)
        text_items = self.find_element(element=output, locator=locators.TextBoxPage.TEXT_ITEM).element_handles()
        return text_items

    def find_field_error(self, locator=locators.TextBoxPage.FILED_ERROR):
        page_logger.info('Finding error locator for current page.')
        return self.find_element(locator=locator).count()
