import pytest
import allure
import requests
import helpers
from data import Urls, ResponsesText


class TestChangeData:
    @allure.title('Изменение данных авторизованного пользователя')
    @allure.description('Проверяем, что авторизованный пользователь может изменить почту, пароль или имя')
    @pytest.mark.parametrize("field", ["password", "email", "name"])
    def test_change_auth_user_data(self, user, field):
        access_token = helpers.register_get_access_token(user)
        changes = {
            "email": user['password'],
            "password": user['name'],
            "name": user['email']
        }
        user[field] = changes[field]
        change_response = requests.patch(Urls.CHANGE_USER_DATA, json=changes, headers={'Authorization': access_token})
        assert change_response.status_code == 200 and change_response.json()['success'] is True

    @allure.title('Изменение данных неавторизованного пользователя')
    @allure.description('Проверяем, что неавторизованный пользователь не может изменить почту, пароль или имя')
    @pytest.mark.parametrize("field", ["password", "email", "name"])
    def test_change_not_auth_user_data(self, user, field):
        register_response = requests.post(Urls.REGISTER_NEW_USER, json=user)
        changes = {
            "email": user['password'],
            "password": user['name'],
            "name": user['email']
        }
        user[field] = changes[field]
        change_response = requests.patch(Urls.CHANGE_USER_DATA, json=changes)
        assert (change_response.status_code == 401 and change_response.json()['message'] ==
                ResponsesText.CHANGE_USER_WITHOUT_AUTH)
