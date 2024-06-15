class BasePage:

    FOOTER = 'footer'
    SUB_ELEMENTS_LIST = '.element-list'
    SUB_ELEMENTS_ITEM = 'li'


class MainPageLocators(BasePage):
    BANNER = '.home-banner'
    CARD_ITEM = '.top-card'
    CARD_BODY = '.card-body'
    LINK = 'a'


class ElementsPage(BasePage):
    ELEMENTS_LIST = '.element-group'


class TextBoxPage(BasePage):
    FULL_NAME = '#userName'
    EMAIL = '#userEmail'
    CURRENT_ADDRESS = '#currentAddress'
    PERMANENT_ADDRESS = '#permanentAddress'
    SUBMIT = '#submit'
    OUTPUT = '#output'
    TEXT_ITEM = 'p'
    FILED_ERROR = '.field-error'
