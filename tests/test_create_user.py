import pytest
import allure
import requests
from helpers import generate_user_credentials
from data import Urls, ResponsesText


class TestCreateUser:
    @allure.title('Создание юзера')
    @allure.description('Проверяем создание юзера с обязательными параметрами')
    def test_create_user(self, user):
        response = requests.post(Urls.REGISTER_NEW_USER, json=user)
        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title('Создание двух одинаковых юзеров')
    @allure.description('Проверяем, что при создании двух одинаковых юзеров возвращается ошибка ')
    def test_create_dup_user(self, user):
        first_response = requests.post(Urls.REGISTER_NEW_USER, json=user)
        second_response = requests.post(Urls.REGISTER_NEW_USER, json=user)
        assert second_response.status_code == 403 and second_response.json()['success'] is False

    @allure.title('Создание юзера без обязательного поля')
    @allure.description('Проверяем, что при создании юзера без почты, логина или пароля возвращается ошибка')
    @pytest.mark.parametrize('required_field', ['email', 'password', 'name'])
    def test_create_user_without_email(self, required_field):
        credentials = generate_user_credentials()
        del credentials[required_field]
        response = requests.post(Urls.REGISTER_NEW_USER, json=credentials)
        assert (response.status_code == 403 and response.json()['message'] ==
                ResponsesText.REGISTER_USER_WITHOUT_REQUIRED_FIELD)
