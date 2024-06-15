import pytest
import test_data
from pages import TextBoxPage


def test_text_box_page(browser):
    text_page = TextBoxPage(browser.new_page())
    text_page.go_to_text_box_page()
    footer = text_page.get_page_footer()

    assert text_page.get_current_url() == test_data.TextBoxPage.EXP_URL
    assert text_page.get_page_title() == test_data.TextBoxPage.EXP_TITLE
    assert footer.text_content() == test_data.TextBoxPage.EXP_FOOTER


def test_text_field(browser):
    text_page = TextBoxPage(browser.new_page())
    text_page.go_to_text_box_page()

    text_dict = {'full_name': 'test_user', 'email': 'test@email.com',
                 'current_address': 'some_address', 'permanent_address': 'another_address'}
    text_page.fill_text_fields(text_dict)
    text_items = text_page.read_output()
    text_items = [item.text_content().split(':')[-1].strip() for item in text_items]

    for value in text_dict.values():
        assert value in text_items


def test_field_validation_error(browser):
    text_page = TextBoxPage(browser.new_page())
    text_page.go_to_text_box_page()

    text_dict = {'email': 'email.com'}
    text_page.fill_text_fields(text_dict)
    n_errors = text_page.find_field_error()
    assert n_errors


if __name__ == '__main__':
    pytest.main()
