import allure

from .base_page import BasePage
from ..url_config import UrlConfig
from ..constants import TestData
from ..locators import RecoveryPageLocators


class RecoveryPage(BasePage):

    @allure.step('Открыть страницу "Восстановления пароля')
    def get_recovery_page(self):
        self.go_to_page(UrlConfig.DOMAIN + UrlConfig.RECOVERY_PASSWORD)

    def click_email_field(self):
        self.driver.find_element(*RecoveryPageLocators.EMAIL_FIELD).click()

    def input_email_to_field(self):
        self.driver.find_element(*RecoveryPageLocators.EMAIL_FIELD).send_keys(
            TestData.EMAIL
        )

    @allure.step('Нажать кнопку "Восстановить')
    def click_recovery_button(self):
        self.driver.find_element(*RecoveryPageLocators.RECOVERY_BUTTON).click()

    @allure.step("Ввести почту в поле email")
    def set_email_to_field(self):
        self.click_email_field()
        self.input_email_to_field()

    @allure.step('Проверить, что текущая страница - страница "Восстановление пароля"')
    def check_current_url_recovery_password(self):
        assert self.get_current_url() == UrlConfig.DOMAIN + UrlConfig.RECOVERY_PASSWORD
