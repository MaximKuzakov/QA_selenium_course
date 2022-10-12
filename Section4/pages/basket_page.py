from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_has_empty_text(self):
        assert len(self.browser.find_elements(*BasketPageLocators.TEXT_BAR)) == 1, 'No text'

    def basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.CHECKOUT_BUTTON), 'Basket is not empty'
