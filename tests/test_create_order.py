import allure
import requests
import helpers
from data import Urls, ResponsesText


class TestCreateOrder:
    @allure.title('Проверка cоздания заказа с авторизованным юзером')
    def test_create_order_by_auth_user(self, user):
        ingredient_list = []
        access_token = helpers.register_get_access_token(user)
        ingredients_response = requests.get(Urls.GET_INGREDIENTS)
        ingredient_id = ingredients_response.json()['data'][0]['_id']
        ingredient_list.append(ingredient_id)
        order_data = {"ingredients": ingredient_list}
        order_response = requests.post(Urls.CREATE_ORDER, json=order_data, headers={'Authorization': access_token})
        assert order_response.status_code == 200 and "order" in order_response.json()

    @allure.title('Проверка создания заказа с неавторизованным юзером')
    def test_create_order_by_not_auth_user(self, user):
        ingredient_list = []
        register_response = requests.post(Urls.REGISTER_NEW_USER, json=user)
        ingredients_response = requests.get(Urls.GET_INGREDIENTS)
        ingredient_id = ingredients_response.json()['data'][0]['_id']
        ingredient_list.append(ingredient_id)
        order_data = {"ingredients": ingredient_list}
        order_response = requests.post(Urls.CREATE_ORDER, json=order_data)
        assert order_response.status_code == 200 and "order" in order_response.json()

    @allure.title('Проверка создания заказа без ингредиентов')
    def test_create_order_without_ingredients(self, user):
        ingredient_list = []
        access_token = helpers.register_get_access_token(user)
        order_data = {"ingredients": ingredient_list}
        order_response = requests.post(Urls.CREATE_ORDER, json=order_data, headers={'Authorization': access_token})
        assert (order_response.status_code == 400 and order_response.json()["message"] ==
                ResponsesText.CREATE_ORDER_WITHOUT_INGREDIENTS)

    @allure.title('Проверка создания заказа с неверным хешем ингредиента')
    def test_create_order_with_invalid_ingredient(self, user):
        ingredient_list = ["1111111111"]
        access_token = helpers.register_get_access_token(user)
        order_data = {"ingredients": ingredient_list}
        order_response = requests.post(Urls.CREATE_ORDER, json=order_data, headers={'Authorization': access_token})
        assert order_response.status_code == 500
