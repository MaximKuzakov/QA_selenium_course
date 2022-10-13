from .base_page import BasePage
from .locators import LoginPageLocators
from time import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'Uncorrect URL'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_BTN), 'login button not present'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_BTN), 'registr button not present'

    def register_new_user(self, email=str(time())+"@fakemail.org", password='Q10W12E14'):
        self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_LOCATOR).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PSWD1_LOCATOR).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PSWD2_LOCATOR).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BTN).click()
