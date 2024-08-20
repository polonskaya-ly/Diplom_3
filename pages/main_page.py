import allure
from selenium.webdriver import ActionChains

from .base_page import BasePage
from ..url_config import UrlConfig
from ..locators import MainPageLocators


class MainPage(BasePage):

    def wait_for_load_authorised_main_page(self):
        self.wait_for_element_presented(MainPageLocators.ORDER_BUTTON)

    @allure.step('Нажать на кнопку перехода в раздел "Личный кабинет')
    def click_account_button(self):
        self.wait_for_load_authorised_main_page()
        self.driver.find_element(*MainPageLocators.ACCOUNT_BUTTON).click()

    @allure.step('Нажать на кнопку перехода в раздел "Лента заказов')
    def click_order_feed(self):
        self.driver.find_element(*MainPageLocators.ORDER_FEED).click()

    def wait_for_load_constructor_header(self):
        self.wait_for_element_presented(MainPageLocators.CONSTRUCTOR_HEADER)

    def wait_for_ingredient_is_clickable(self):
        self.wait_for_element_clickable(MainPageLocators.INGREDIENT)

    def wait_for_invisibility_cross_icon(self):
        self.wait_for_element_not_presented(MainPageLocators.CROSS_ICON)

    @allure.step("Нажать на ингредиент")
    def click_ingredient(self):
        self.wait_for_ingredient_is_clickable()
        self.driver.find_element(*MainPageLocators.INGREDIENT).click()

    def wait_for_pop_up_ingredient_visible(self):
        self.wait_for_element_presented(MainPageLocators.CROSS_ICON)

    @allure.step("Нажать на иконку крестика")
    def click_cross_icon(self):
        self.wait_for_pop_up_ingredient_visible()
        self.driver.find_element(*MainPageLocators.CROSS_ICON).click()

    @allure.step("Перетащить ингредиент в корзину")
    def drug_and_drop_ingredient_to_cart(self):
        self.wait_for_ingredient_is_clickable()
        action = ActionChains(self.driver)
        source_element = self.driver.find_element(*MainPageLocators.INGREDIENT)
        target_element = self.driver.find_element(*MainPageLocators.BASKET)
        action.drag_and_drop(source_element, target_element)
        action.perform()

    def wait_for_change_basket_image(self):
        self.wait_for_element_not_presented(MainPageLocators.BASKET_FREE_IMAGE)

    def wait_for_order_modal_displayed(self):
        self.wait_for_element_presented(MainPageLocators.ORDER_IDENTIFICATOR_MESSAGE)

    def wait_for_order_default_is_not_displayed(self):
        self.wait_for_element_not_presented(MainPageLocators.ORDER_NUMBER_DEFAULT)

    def click_order_button(self):
        self.wait_for_change_basket_image()
        self.driver.find_element(*MainPageLocators.ORDER_BUTTON).click()

    @allure.step("Создать заказ")
    def create_order(self):
        self.drug_and_drop_ingredient_to_cart()
        self.click_order_button()

    @allure.step("Получить номер созданного заказа")
    def get_order_number(self):
        self.wait_for_order_modal_displayed()
        self.wait_for_order_default_is_not_displayed()
        order_number = self.driver.find_element(*MainPageLocators.ORDER_NUMBER).text
        return order_number

    @allure.step("Открыть главную страницу с конструктором")
    def get_main_page(self):
        self.go_to_page(UrlConfig.DOMAIN)
        self.wait_for_load_authorised_main_page()

    @allure.step("Проверить, что pop up ингредиента отображается")
    def check_pop_up_ingredient_is_displayed(self):
        self.wait_for_pop_up_ingredient_visible()
        assert self.driver.find_element(
            *MainPageLocators.INGREDIENT_POP_UP
        ).is_displayed()

    @allure.step("Проверить, что pop up ингредиента не отображается")
    def check_pop_up_ingredient_is_not_displayed(self):
        self.wait_for_invisibility_cross_icon()
        assert not self.driver.find_element(
            *MainPageLocators.INGREDIENT_POP_UP
        ).is_displayed()

    @allure.step("Проверить значение счетчика ингредиента")
    def check_ingredient_counter_number(self):
        self.wait_for_change_basket_image()
        assert (
            self.driver.find_element(*MainPageLocators.INGREDIENT_COUNTER).text == "2"
        )

    @allure.step("Проверить, что текущая страница главная")
    def check_current_url_main(self):
        self.wait_for_load_constructor_header()
        assert self.get_current_url() == UrlConfig.DOMAIN

    @allure.step("Проверить сообщение на pop up нового заказа")
    def check_order_pop_up_message(self):
        self.wait_for_order_modal_displayed()
        assert (
            self.driver.find_element(*MainPageLocators.ORDER_POP_UP_MESSAGE).text
            == "Ваш заказ начали готовить"
        )
