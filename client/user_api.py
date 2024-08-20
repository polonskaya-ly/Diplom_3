import requests
from ..url_config import UrlConfig
import allure


url = UrlConfig.DOMAIN


class UserApi:
    @allure.step("Зарегистриовать пользователя")
    def post_register(self, payload):
        response = requests.post(url + UrlConfig.API_REGISTER, data=payload)
        return response

    @allure.step("Удалить пользователя")
    def delete_user(self, headers):
        response = requests.delete(url + UrlConfig.API_USER, headers=headers)
        return response
