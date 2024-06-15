import pytest
import test_data
from pages import MainPage


def test_main_page(browser):
    main_page = MainPage(browser.new_page())
    main_page.go_to_main_page()
    footer = main_page.get_footer()

    assert main_page.get_current_url() == test_data.MainPage.EXP_URL
    assert main_page.get_title() == test_data.MainPage.EXP_TITLE
    assert footer.text_content() == test_data.MainPage.EXP_FOOTER


def test_main_page_elements(browser):
    main_page = MainPage(browser.new_page())
    main_page.go_to_main_page()

    elements = main_page.get_list_of_cards()
    cards = [element.text_content() for element in elements]
    assert cards == test_data.MainPage.EXP_CARDS


def test_main_page_banner(browser):
    main_page = MainPage(browser.new_page())
    main_page.go_to_main_page()
    banner = main_page.get_banner()

    link = main_page.find_banner_link(element=banner)
    assert link.get_attribute('href') == test_data.MainPage.EXP_BANNER_URL


if __name__ == '__main__':
    pytest.main()

