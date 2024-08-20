import pytest
import random
import allure
from selenium import webdriver

from .client.user_api import UserApi
from .constants import TestData
from .pages.feed_page import FeedPage
from .pages.main_page import MainPage
from .pages.account_page import AccountPage
from .pages.login_page import LoginPage
from .pages.recovery_page import RecoveryPage
from .pages.reset_page import ResetPage
from .url_config import UrlConfig


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(UrlConfig.DOMAIN)
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture
@allure.step('Перейти на страницу ввода нового пароля')
def get_reset_page(driver):
    recovery_page = RecoveryPage(driver)
    recovery_page.get_recovery_page()
    recovery_page.set_email_to_field()
    recovery_page.click_recovery_button()
    reset_page = ResetPage(driver)
    reset_page.wait_for_load_password_field()


@pytest.fixture
def login(driver, email=TestData.EMAIL):
    login_page = LoginPage(driver)
    login_page.login(email)


@pytest.fixture
@allure.step('Перейти в личный кабинет')
def move_to_account(driver, login):
    main_page = MainPage(driver)
    main_page.click_account_button()
    account_page = AccountPage(driver)
    account_page.wait_for_load_profile_header()


@pytest.fixture
def get_login_page(driver):
    login_page = LoginPage(driver)
    login_page.get_login_page()


@pytest.fixture
def get_feed_page(driver):
    feed_page = FeedPage(driver)
    feed_page.get_feed_page()
    feed_page.wait_for_load_feed_header()


@pytest.fixture
@allure.step('Получить значение счетчиков до офорлмения заказа')
def get_counters_orders(driver, get_feed_page):
    feed_page = FeedPage(driver)
    total_counter = feed_page.get_total_counter()
    today_counter = feed_page.get_today_counter()
    return total_counter, today_counter


@pytest.fixture
def register_data():
    name = f'Любовь{random.randint(1000, 9999)}'
    email = f'polonskaya{random.randint(1000, 9999)}@yandex.ru'
    return name, email


@pytest.fixture
def register_user_and_login(register_data, driver):
    payload = {
        "name": register_data[0],
        "password": TestData.PASSWORD,
        "email": register_data[1],
    }
    response = UserApi().post_register(payload)
    r = response.json()
    token = r["accessToken"]
    headers = {"Authorization": token}
    login_page = LoginPage(driver)
    login_page.login(register_data[1])
    main_page = MainPage(driver)
    main_page.wait_for_load_authorised_main_page()
    yield headers
    UserApi().delete_user(headers)


@pytest.fixture
def create_order(driver):
    main_page = MainPage(driver)
    main_page.create_order()
    order_number = main_page.get_order_number()
    return order_number
