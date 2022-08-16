from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
    BASKET_BTN = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > "
                                   "span > a")


class BasketPageLocators():
    BASKET_PRODUCT_PRICE = (By.CSS_SELECTOR, "#basket_totals > table > tbody > tr:nth-child(2) > th.total.align-right")
    BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, "#basket_formset > div > div > div.col-sm-4 > h3 > a")
