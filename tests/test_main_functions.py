import allure
import pytest

from ..pages.login_page import LoginPage
from ..pages.feed_page import FeedPage
from ..pages.main_page import MainPage


@pytest.mark.usefixtures("driver")
class TestMainFunctions:
    @allure.title("Переход в раздел «Лента заказов»")
    def test_move_to_order_feed(self):
        main_page = MainPage(self.driver)
        main_page.click_order_feed()
        feed_page = FeedPage(self.driver)
        feed_page.check_current_url_order_feed()

    @allure.title("Переход в раздел «Конструктор»")
    def test_move_to_constructor(self, get_login_page):
        login_page = LoginPage(self.driver)
        login_page.click_constructor_button()
        main_page = MainPage(self.driver)
        main_page.check_current_url_main()

    @allure.title("Получение pop up для ингредиента по клику на ингредиент")
    def test_ingredient_pop_up_by_click_ingredient(self):
        main_page = MainPage(self.driver)
        main_page.click_ingredient()
        main_page.check_pop_up_ingredient_is_displayed()

    @allure.title("Закрытие pop up ингредиента по крестику")
    def test_close_pop_up_ingredient_by_cross_icon(self):
        main_page = MainPage(self.driver)
        main_page.click_ingredient()
        main_page.click_cross_icon()
        main_page.check_pop_up_ingredient_is_not_displayed()

    @allure.title("Увеличение каунтера ингредиента при добавлении в заказ ингредиента")
    def test_ingredient_counter_by_adding_ingredient_to_cart(self):
        main_page = MainPage(self.driver)
        main_page.drug_and_drop_ingredient_to_cart()
        main_page.check_ingredient_counter_number()

    @allure.title("Создание заказа авторизованным пользователем")
    def test_create_order_by_authorised_user(self, login):
        main_page = MainPage(self.driver)
        main_page.create_order()
        main_page.check_order_pop_up_message()
