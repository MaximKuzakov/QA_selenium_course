from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_BTN = (By.NAME, 'login_submit')
    REGISTRATION_BTN = (By.NAME, 'registration_submit')
    REGISTRATION_EMAIL_LOCATOR = (By.NAME, "registration-email")
    REGISTRATION_PSWD1_LOCATOR = (By.NAME, "registration-password1")
    REGISTRATION_PSWD2_LOCATOR = (By.NAME, "registration-password2")


class ProductPageLocators:
    ADD_ITEM = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
    PRICE_ITEM = (By.CSS_SELECTOR, '.col-sm-6.product_main .price_color')
    TITLE_ITEM = (By.CSS_SELECTOR, '.col-sm-6.product_main h1')
    ELEMENTS = (By.CSS_SELECTOR, '.alertinner strong')


class BasketPageLocators:
    TEXT_BAR = (By.CSS_SELECTOR, "#content_inner p")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-block")