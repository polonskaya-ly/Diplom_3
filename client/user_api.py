import requests
from ..url_config import UrlConfig
import allure


url = UrlConfig.domain


class UserApi:
    @allure.step("Зарегистриовать пользователя")
    def post_register(self, payload):
        response = requests.post(url + UrlConfig.api_register, data=payload)
        return response

    @allure.step("Удалить пользователя")
    def delete_user(self, headers):
        response = requests.delete(url + UrlConfig.api_user, headers=headers)
        return response
