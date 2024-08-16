import allure
import pytest

from ..pages.reset_page import ResetPage
from ..pages.recovery_page import RecoveryPage
from ..pages.login_page import LoginPage


@pytest.mark.usefixtures("driver")
class TestRecoverPassword:
    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_move_to_recovery_password_page(self):
        login_page = LoginPage(self.driver)
        login_page.get_login_page()
        login_page.click_recovery_password_button()
        recovery_page = RecoveryPage(self.driver)
        recovery_page.check_current_url_recovery_password()

    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    def test_move_to_reset_page(self):
        recovery_page = RecoveryPage(self.driver)
        recovery_page.get_recovery_page()
        recovery_page.set_email_to_field()
        recovery_page.click_recovery_button()
        reset_page = ResetPage(self.driver)
        reset_page.check_current_url_reset_password()
    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным')
    def test_make_password_field_active_with_eye(self, get_reset_page):
        reset_page = ResetPage(self.driver)
        reset_page.click_password_eye()
        reset_page.check_password_field_active()
