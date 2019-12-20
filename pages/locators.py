
from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_URL = "login"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    BTN_WRITE_REVIEW = (By.CSS_SELECTOR, "#write_review")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")
    MESSAGES_PRODUCT_NAME = (By.CSS_SELECTOR, ".alertinner>strong")
    MESSAGES_PRODUCT_PRICE = (By.CSS_SELECTOR, ".alertinner>p>strong")

