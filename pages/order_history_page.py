import allure

from .base_page import BasePage
from ..locators import OrderHistoryPageLocators
from ..url_config import UrlConfig


class OrderHistoryPage(BasePage):

    def wait_for_load_order_card(self):
        self.wait_for_element_presented(OrderHistoryPageLocators.ORDER_CARD)

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
        assert self.get_current_url() == UrlConfig.DOMAIN + UrlConfig.ORDER_HISTORY
