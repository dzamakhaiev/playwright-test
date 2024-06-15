import pytest
import test_data
from pages import MainPage


def test_main_page(browser):
    main_page = MainPage(browser.new_page())
    main_page.go_to_main_page()
    footer = main_page.get_footer()
    assert main_page.get_title() == test_data.MainPage.EXP_TITLE
    assert footer.text_content() == test_data.MainPage.EXP_FOOTER


if __name__ == '__main__':
    pytest.main()

