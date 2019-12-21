
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.browser.find_element(
            *LoginPageLocators.LOGIN_REGISTER_EMAIL).send_keys(email)
        self.browser.find_element(
            *LoginPageLocators.LOGIN_REGISTER_PASSWORD1).send_keys(password)
        self.browser.find_element(
            *LoginPageLocators.LOGIN_REGISTER_PASSWORD2).send_keys(password)
        self.browser.find_element(
            *LoginPageLocators.BTN_REGISTER).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert (
            LoginPageLocators.LOGIN_URL in self.browser.current_url), \
            "Missing login in URL"

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM), "Login Form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_REGISTER_FORM), \
            "Register Form is not presented"
