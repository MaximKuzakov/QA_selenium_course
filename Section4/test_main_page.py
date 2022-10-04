from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    # link2 = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    # page2 = LoginPage(browser, link2)
    # page2.open()
