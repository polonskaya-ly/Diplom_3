import pytest
import allure

from ..pages.order_history_page import OrderHistoryPage
from ..pages.account_page import AccountPage
from ..pages.main_page import MainPage
from ..pages.feed_page import FeedPage


@pytest.mark.usefixtures("driver")
class TestOrderFeed:
    @allure.title("Открытие pop up с деталями заказа по клику на заказ")
    def test_pop_up_order_details(self, get_feed_page):
        feed_page = FeedPage(self.driver)
        feed_page.click_order()
        feed_page.check_order_details_is_displayed()

    @allure.title('Новый заказ появляется в разделе "В работе"')
    def test_new_order_status_in_work(self, login, create_order):
        order_number = create_order
        feed_page = FeedPage(self.driver)
        feed_page.get_feed_page()
        feed_page.check_order_number_in_work_status(order_number)

    @allure.title('При создании заказа счетчик "Выполнено за все время" увеличивается')
    def test_total_counter(self, get_counters_orders, login, create_order):
        feed_page = FeedPage(self.driver)
        feed_page.get_feed_page()
        feed_page.check_total_counter_after_created_order(get_counters_orders[0])

    @allure.title('При создании заказа счетчик "Выполнено за сегодня" увеличивается')
    def test_today_counter(self, get_counters_orders, login, create_order):
        feed_page = FeedPage(self.driver)
        feed_page.get_feed_page()
        feed_page.check_today_counter_after_created_order(get_counters_orders[1])

    @allure.title(
        'Заказы пользователя из раздела «История заказов» отображаются на странице "Лента заказов"'
    )
    def test_order_feed_include_order_history_user(
        self, register_user_and_login, create_order
    ):
        main_page = MainPage(self.driver)
        main_page.get_main_page()
        main_page.click_account_button()
        account_page = AccountPage(self.driver)
        account_page.click_history_button()
        order_history_page = OrderHistoryPage(self.driver)
        order_number = order_history_page.get_order_history_order_number()
        order_history_page.click_order_feed()
        feed_page = FeedPage(self.driver)
        feed_page.check_order_feed_include_order_history_user(order_number)
