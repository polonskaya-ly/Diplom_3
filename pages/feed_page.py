import allure
from selenium.webdriver.common.by import By

from .base_page import BasePage
from ..locators import FeedPageLocators
from ..url_config import UrlConfig


class FeedPage(BasePage):

    def wait_for_load_feed_header(self):
        self.wait_for_element_presented(FeedPageLocators.FEED_HEADER)

    def wait_for_load_order_content(self):
        self.wait_for_element_presented(FeedPageLocators.ORDER_CONTENT)

    @allure.step('Открыть страницу "Лента заказов')
    def get_feed_page(self):
        self.go_to_page(UrlConfig.DOMAIN + UrlConfig.FEED)
        self.wait_for_load_feed_header()

    @allure.step("Нажать на первый заказ в списке")
    def click_order(self):
        self.wait_for_load_feed_header()
        self.driver.find_element(*FeedPageLocators.ORDER).click()

    def wait_for_work_status_changed(self):
        self.wait_for_element_not_presented(FeedPageLocators.READY_MESSAGE_FOR_ORDERS)

    @allure.step('Получить значение счетчика "Выполнено за все время"')
    def get_total_counter(self):
        total_counter = self.driver.find_element(*FeedPageLocators.TOTAL_ORDERS).text
        total_counter = int(total_counter)
        return total_counter

    def scroll_to_today_counter(self):
        element = self.driver.find_element(*FeedPageLocators.TODAY_ORDERS)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Получить значение счетчика "Выполнено за сегодня"')
    def get_today_counter(self):
        self.scroll_to_today_counter()
        today_counter = self.driver.find_element(*FeedPageLocators.TODAY_ORDERS).text
        today_counter = int(today_counter)
        return today_counter

    @staticmethod
    def get_order_number_locator(order_number):
        order_number_locator = [By.XPATH, f'.//p[contains(text(), "{order_number}")]']
        return order_number_locator

    @staticmethod
    def get_total_current_order_counter_locator(total_counter):
        total_order_counter_locator = [
            By.XPATH,
            f'.//p[contains(text(),"Выполнено за сегодня")]/'
            f'parent::div/p[contains(@text, "{total_counter}")]',
        ]
        return total_order_counter_locator

    @staticmethod
    def get_today_current_order_counter_locator(today_counter):
        total_order_counter_locator = [
            By.XPATH,
            f'.//p[contains(text(),"Выполнено за сегодня")]/'
            f'parent::div/p[contains(@text, "{today_counter}")]',
        ]
        return total_order_counter_locator

    def wait_current_total_counter_is_not_visible(self, total_counter):
        self.wait_for_element_not_presented(
            self.get_today_current_order_counter_locator(total_counter)
        )

    def wait_current_today_counter_is_not_visible(self, today_counter):
        self.wait_for_element_not_presented(
            self.get_today_current_order_counter_locator(today_counter)
        )

    @allure.step('Проверить, что новый заказ отображается в колонке "В работе')
    def check_order_number_in_work_status(self, order_number):
        self.wait_for_work_status_changed()
        assert (
            order_number in self.driver.find_element(*FeedPageLocators.WORK_STATUS).text
        )

    @allure.step('Проверить, что текущая страница - страница "Лента заказов')
    def check_current_url_order_feed(self):
        self.wait_for_load_feed_header()
        assert self.get_current_url() == UrlConfig.DOMAIN + UrlConfig.FEED

    @allure.step("Проверить, что детали заказа открылись в pop up")
    def check_order_details_is_displayed(self):
        self.wait_for_load_order_content()
        assert self.driver.find_element(
            *FeedPageLocators.ORDER_DETAILS_POP_UP
        ).is_displayed()

    @allure.step('Проверить, что счетчик "Выполненео за все время" увеличился')
    def check_total_counter_after_created_order(self, total_counter):
        total_counter = int(total_counter)
        self.wait_current_total_counter_is_not_visible(total_counter)
        assert self.get_total_counter() > total_counter

    @allure.step('Проверить, что счетчик "Выполненео за сегодня" увеличился')
    def check_today_counter_after_created_order(self, today_counter):
        today_counter = int(today_counter)
        self.wait_current_today_counter_is_not_visible(today_counter)
        assert self.get_today_counter() > today_counter

    @allure.step(
        'Проверить, что заказ из "История заказов" содержится в списке в "Лента заказов'
    )
    def check_order_feed_include_order_history_user(self, order_number):
        self.wait_for_load_feed_header()
        assert self.driver.find_element(
            *self.get_order_number_locator(order_number)
        ).is_displayed()
