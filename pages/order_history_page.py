import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from ..helper import Helper
from ..locators import OrderHistoryPageLocators
from ..url_config import UrlConfig


class OrderHistoryPage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_order_card(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (OrderHistoryPageLocators.ORDER_CARD)
            )
        )

    @allure.step('Получить номер заказа в разделе "История заказов"')
    def get_order_history_order_number(self):
        self.wait_for_load_order_card()
        order_number = self.driver.find_element(
            *OrderHistoryPageLocators.ORDER_NUMBER
        ).text
        return order_number

    @allure.step('Перейти в раздел "Лента заказов"')
    def click_order_feed(self):
        self.driver.find_element(*OrderHistoryPageLocators.ORDER_FEED_BUTTON).click()

    @allure.step('Проверить, что текущая страница - раздела "История заказов"')
    def check_current_url_order_history(self):
        assert (
            Helper(self.driver).get_current_url()
            == UrlConfig.domain + UrlConfig.order_history_path
        )
