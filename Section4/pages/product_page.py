from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_ITEM).click()
        self.solve_quiz_and_get_code()
        self.title = self.browser.find_element(*ProductPageLocators.TITLE_ITEM).text
        self.price = self.browser.find_element(*ProductPageLocators.PRICE_ITEM).text
        elements = self.browser.find_elements(*ProductPageLocators.ELEMENTS)
        assert elements[0].text == self.title, 'Title is not right'
        assert elements[2].text == self.price, 'Price is not right'

