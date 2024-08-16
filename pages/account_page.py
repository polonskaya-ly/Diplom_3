import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from ..helper import Helper
from ..locators import AccountPageLocators
from ..url_config import UrlConfig


class AccountPage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_profile_header(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((AccountPageLocators.
                                                                                               PROFILE_HEADER)))

    @allure.step('Нажать на кнопку "История заказов"')
    def click_history_button(self):
        self.wait_for_load_profile_header()
        self.driver.find_element(*AccountPageLocators.HISTORY_BUTTON).click()

    @allure.step('Нажать на кнопку "Выход"')
    def click_logout_button(self):
        self.driver.find_element(*AccountPageLocators.LOGOUT_BUTTON).click()

    @allure.step('Проверить, что текущая страница - страница личного кабинета')
    def check_current_url_profile_account(self):
        self.wait_for_load_profile_header()
        assert Helper(self.driver).get_current_url() == UrlConfig.domain + UrlConfig.account_path






