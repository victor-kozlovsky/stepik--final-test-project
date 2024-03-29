
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        btn_add_to_basket = self.browser.find_element(
            *ProductPageLocators.BTN_ADD_TO_BASKET)
        btn_add_to_basket.click()

    def cant_see_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def get_product_name(self):
        return self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE).text

    def should_be_btn_add_to_basket(self):
        assert self.is_element_present(
            *ProductPageLocators.BTN_ADD_TO_BASKET), \
            "Button add to basket is not presented"

    def should_be_btn_write_review(self):
        assert self.is_element_present(
            *ProductPageLocators.BTN_WRITE_REVIEW), \
            "Button write review is not presented"

    def should_be_correct_product_added(self, product, price):
        msg_product = self.browser.find_element(
            *ProductPageLocators.MESSAGES_PRODUCT_NAME).text
        msg_price = self.browser.find_element(
            *ProductPageLocators.MESSAGES_PRODUCT_PRICE).text
        assert (product == msg_product and price == msg_price), \
            "Added product not correct"

    def success_message_disappeared(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message cant disappeared"
