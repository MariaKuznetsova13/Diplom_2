import allure
import requests
from faker import Faker
import random
import string
from data import Urls

faker_ru = Faker('ru_RU')


@allure.step("Генерируем креды для регистрации юзера")
def generate_user_credentials():
    def generate_email():
        email = faker_ru.email()
        split = email.split("@")
        return split[0] + "+" + str(random.randint(1000, 99999999)) + "@" + split[1]

    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    email = generate_email()
    password = generate_random_string(10)
    name = generate_random_string(10)

    credentials = {
        "email": email,
        "password": password,
        "name": name
    }

    return credentials


@allure.step("Извлекаем данные для авторизации юзера")
def get_data_for_auth(credentials):
    return {
        'email': credentials['email'],
        'password': credentials['password']
    }


@allure.step("Регистрируем юзера и получаем его accessToken")
def register_get_access_token(credentials):
    register_response = requests.post(Urls.REGISTER_NEW_USER, json=credentials)
    access_token = register_response.json().get('accessToken')
    return access_token


@allure.step("Авторизуем юзера и получаем его accessToken")
def login_user(credentials):
    data_for_login = get_data_for_auth(credentials)
    login_response = requests.post(Urls.LOGIN_USER, json=data_for_login)
    access_token = login_response.json().get('accessToken')
    return access_token


@allure.step("Удаляем юзера")
def delete_user(credentials):
    access_token = login_user(credentials)
    delete_response = requests.delete(Urls.DELETE_USER, headers={'Authorization': access_token})
    return delete_response
