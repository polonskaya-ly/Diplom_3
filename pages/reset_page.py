import allure

from .base_page import BasePage
from ..locators import ResetPageLocators

from ..url_config import UrlConfig


class ResetPage(BasePage):

    def wait_for_load_password_field(self):
        self.wait_for_element_presented(ResetPageLocators.PASSWORD_FIELD)

    @allure.step("Нажать на иконку глаза")
    def click_password_eye(self):
        self.driver.find_element(*ResetPageLocators.ICON_EYE).click()

    @allure.step("Проверить, что текущая страница - страница для ввода нового пароля")
    def check_current_url_reset_password(self):
        self.wait_for_load_password_field()
        assert self.get_current_url() == UrlConfig.DOMAIN + UrlConfig.RESET_PASSWORD

    @allure.step("Проверить, что поле ввода пароля стало активным")
    def check_password_field_active(self):
        assert self.driver.find_element(
            *ResetPageLocators.PASSWORD_FIELD_ACTIVE
        ).is_displayed()
