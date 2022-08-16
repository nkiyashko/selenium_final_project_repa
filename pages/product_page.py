
from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import BasketPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPage(BasePage):
    def add_to_cart(self):
        login_link = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        login_link.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def open_basket_page(self):
        basket_btn = self.browser.find_element(*ProductPageLocators.BASKET_BTN)
        basket_btn.click()

    def product_name_is_the_same(self):
        prod_name = str(*ProductPageLocators.PRODUCT_NAME)
        basket_name = str(*BasketPageLocators.BASKET_PRODUCT_NAME)
        assert prod_name == basket_name

    def product_price_is_the_same(self, browser):
        prod_price = browser.(*ProductPageLocators.PRODUCT_PRICE)
        basket_price = str(*BasketPageLocators.BASKET_PRODUCT_PRICE)
        assert prod_price == basket_price
