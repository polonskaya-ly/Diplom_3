import allure

from ..helper import Helper
from ..url_config import UrlConfig
from ..constants import TestData
from ..locators import RecoveryPageLocators


class RecoveryPage:
    def __init__(self, driver):
        self.driver = driver

    def get_recovery_page(self):
        self.driver.get(UrlConfig.domain + UrlConfig.recovery_password_path)

    def click_email_field(self):
        self.driver.find_element(*RecoveryPageLocators.EMAIL_FIELD).click()

    def input_email_to_field(self):
        self.driver.find_element(*RecoveryPageLocators.EMAIL_FIELD).send_keys(
            TestData.email
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
        assert (
            Helper(self.driver).get_current_url()
            == UrlConfig.domain + UrlConfig.recovery_password_path
        )
