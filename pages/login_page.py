import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from ..helper import Helper
from ..constants import TestData
from ..url_config import UrlConfig
from ..locators import LoginPageLocators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def get_login_page(self):
        self.driver.get(UrlConfig.domain + UrlConfig.login_path)

    @allure.step('Нажать на кнопку "Восстановить')
    def click_recovery_password_button(self):
        self.driver.find_element(*LoginPageLocators.RECOVERY_PASSWORD_BUTTON).click()

    def click_email_field(self):
        self.driver.find_element(*LoginPageLocators.EMAIL_FIELD).click()

    def input_email_to_field(self, email):
        self.driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(email)

    def set_email_to_field(self, email):
        self.click_email_field()
        self.input_email_to_field(email)

    def click_password_field(self):
        self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD).click()

    def input_password_to_field(self):
        self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(TestData.password)

    def set_password_to_field(self):
        self.click_password_field()
        self.input_password_to_field()

    def click_login_button(self):
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    def wait_for_login_header_is_displayed(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((LoginPageLocators.
                                                                                               ENTER_HEADER)))

    def click_constructor_button(self):
        self.driver.find_element(*LoginPageLocators.CONSTRUCTOR).click()

    @allure.step("Войти в аккаунт")
    def login(self, email):
        self.get_login_page()
        self.set_email_to_field(email)
        self.set_password_to_field()
        self.click_login_button()

    @allure.step("Проверить, что текущая страница - страница для входа в аккаунт")
    def check_current_url_is_login(self):
        self.wait_for_login_header_is_displayed()
        assert Helper(self.driver).get_current_url() == UrlConfig.domain + UrlConfig.login_path









