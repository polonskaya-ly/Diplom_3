import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from ..helper import Helper
from ..locators import ResetPageLocators

from ..url_config import UrlConfig


class ResetPage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_password_field(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((ResetPageLocators.
                                                                                               PASSWORD_FIELD)))

    @allure.step('Нажать на иконку глаза')
    def click_password_eye(self):
        self.driver.find_element(*ResetPageLocators.ICON_EYE).click()

    @allure.step('Проверить, что текущая страница - страница для ввода нового пароля')
    def check_current_url_reset_password(self):
        self.wait_for_load_password_field()
        assert Helper(self.driver).get_current_url() == UrlConfig.domain + UrlConfig.reset_password_path

    @allure.step('Проверить, что поле ввода пароля стало активным')
    def check_password_field_active(self):
        assert self.driver.find_element(*ResetPageLocators.PASSWORD_FIELD_ACTIVE).is_displayed()
