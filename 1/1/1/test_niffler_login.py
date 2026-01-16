import pytest
from selene import browser, have


@pytest.fixture
def open_browser():
    browser.open('https://niffler.qa.guru')
    yield
    browser.quit()


def login(username, password):
    browser.element('#username').type(username)
    browser.element('#password').type(password)


def test_success_login(open_browser):
    login('stas', '12345')
    browser.element('#login-button').click()

    browser.element('#spendings').should(have.text('History of Spendings'))


def test_success_login_with_press_enter(open_browser):
    login('stas', '12345')
    browser.element('#password').press_enter()

    browser.element('#spendings').should(have.text('History of Spendings'))


def test_wrong_credentials(open_browser):
    login('stas', '12345sgsrgwr')
    browser.element('#password').press_enter()

    browser.element('.form__error').should(have.text('Bad credentials'))
