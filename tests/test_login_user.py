import pytest
import allure
import requests
import helpers
from data import Urls, ResponsesText


class TestLoginUser:
    @allure.title('Логин юзера')
    @allure.description('Проверяем, что существующий юзер успешно авторизуется')
    def test_login_courier(self, user):
        register_response = requests.post(Urls.REGISTER_NEW_USER, json=user)
        auth_data = helpers.get_data_for_auth(user)
        login_response = requests.post(Urls.LOGIN_USER, json=auth_data)
        assert login_response.status_code == 200 and login_response.json()['success'] is True

    @allure.title('Логин юзера с некорректным паролем или логином')
    @allure.description('Проверяем, что при логине с некорректным паролем или логином возвращается ошибка')
    @pytest.mark.parametrize("login_type", ["password", "email"])
    def test_login_with_wrong_credentials(self, user, login_type):
        register_response = requests.post(Urls.REGISTER_NEW_USER, json=user)
        auth_data = helpers.get_data_for_auth(user)
        changes = {
            "password": auth_data['email'],
            "email": auth_data['password']
        }
        auth_data[login_type] = changes[login_type]
        login_response = requests.post(Urls.LOGIN_USER, json=auth_data)
        assert login_response.status_code == 401 and login_response.json()[
            'message'] == ResponsesText.LOGIN_WITH_WRONG_PASSWORD_OR_EMAIL
