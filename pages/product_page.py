from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        login_link = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        login_link.click()

    def open_basket_page(self):
        basket_btn = self.browser.find_element(*ProductPageLocators.BASKET_BTN)
        basket_btn.click()

    def should_be_message_about_adding(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), (
            "Product name is not presented")
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), (
            "Message about adding is not presented")
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING).text
        assert product_name in message, "No product name in the message"

    def should_be_message_basket_total(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_TOTAL), (
            "Message basket total is not presented")
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), (
            "Product price is not presented")
        message_basket_total = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert product_price in message_basket_total, "No product price in the message"
