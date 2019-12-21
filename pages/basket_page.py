
from .base_page import BasePage
from .locators import BasketLocators

class BasketPage(BasePage):
    def should_be_basket_empty(self):
        assert self.is_not_element_present(
            *BasketLocators.BASKET_FILLED), "Basket is not empty"
    
    def should_be_text_that_the_basket_is_empty(self): 
        assert self.is_element_present(
            *BasketLocators.BASKET_EMPTY_TXT), "Should be text that the basket is empty"

