from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_BTN = (By.NAME, 'login_submit')
    REGISTRATION_BTN = (By.NAME, 'registration_submit')
