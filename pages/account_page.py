import allure

from .base_page import BasePage
from ..locators import AccountPageLocators
from ..url_config import UrlConfig


class AccountPage(BasePage):

    def wait_for_load_profile_header(self):
        self.wait_for_element_presented(AccountPageLocators.PROFILE_HEADER)

    @allure.step('Нажать на кнопку "История заказов"')
    def click_history_button(self):
        self.wait_for_load_profile_header()
        self.driver.find_element(*AccountPageLocators.HISTORY_BUTTON).click()

    @allure.step('Нажать на кнопку "Выход"')
    def click_logout_button(self):
        self.driver.find_element(*AccountPageLocators.LOGOUT_BUTTON).click()

    @allure.step("Проверить, что текущая страница - страница личного кабинета")
    def check_current_url_profile_account(self):
        self.wait_for_load_profile_header()
        assert self.get_current_url() == UrlConfig.DOMAIN + UrlConfig.ACCOUNT
