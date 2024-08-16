import pytest
import allure

from ..pages.order_history_page import OrderHistoryPage
from ..pages.login_page import LoginPage
from ..pages.account_page import AccountPage
from ..pages.main_page import MainPage


@pytest.mark.usefixtures("driver")
class TestPersonalAccount:
    @allure.title("Переход по клику на «Личный кабинет»")
    def test_move_to_account_with_account_button(self, login):
        main_page = MainPage(self.driver)
        main_page.click_account_button()
        account_page = AccountPage(self.driver)
        account_page.check_current_url_profile_account()

    @allure.title("Переход в раздел «История заказов»")
    def test_move_to_order_history(self, login, move_to_account):
        account_page = AccountPage(self.driver)
        account_page.click_history_button()
        order_history_page = OrderHistoryPage(self.driver)
        order_history_page.check_current_url_order_history()

    @allure.title("Выход из аккаунта")
    def test_logout_from_account(self, login, move_to_account):
        account_page = AccountPage(self.driver)
        account_page.click_logout_button()
        login_page = LoginPage(self.driver)
        login_page.check_current_url_is_login()
