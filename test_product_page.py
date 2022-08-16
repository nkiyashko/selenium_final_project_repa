import pytest
from .pages.product_page import ProductPage

@pytest.mark.parametrize('url', ["http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo"
                                 "=newYear",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo"
                                 "=newYear2019"])
def test_guest_can_add_product_to_basket(browser, url):
    link = url
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()
