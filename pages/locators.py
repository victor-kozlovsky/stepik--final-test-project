
from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group>a[href*='/basket/']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketLocators():
    BASKET_FILLED = (By.CSS_SELECTOR, ".basket-title")
    BASKET_EMPTY_TXT = (By.CSS_SELECTOR, "#content_inner>p")


class LoginPageLocators():
    LOGIN_URL = "login"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    LOGIN_REGISTER_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    LOGIN_REGISTER_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    BTN_REGISTER = (By.NAME, "registration_submit")
    

class ProductPageLocators():
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BTN_WRITE_REVIEW = (By.CSS_SELECTOR, "#write_review")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    MESSAGES_PRODUCT_NAME = (By.CSS_SELECTOR, ".alertinner>strong:first-child")
    MESSAGES_PRODUCT_PRICE = (By.CSS_SELECTOR, ".alertinner>p>strong")
 
