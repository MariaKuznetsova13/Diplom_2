import allure
import requests
import helpers
from data import Urls, ResponsesText


class TestUserOrders:
    @allure.title('Проверка получения заказов авторизованного юзера')
    def test_get_orders_auth_user(self, user):
        access_token = helpers.register_get_access_token(user)
        response = requests.get(Urls.GET_USER_ORDERS, headers={'Authorization': access_token})
        assert response.status_code == 200 and "orders" in response.json()

    @allure.title('Проверка получения заказов неавторизованного юзера')
    def test_get_orders_not_auth_user(self, user):
        register_response = requests.post(Urls.REGISTER_NEW_USER, json=user)
        response = requests.get(Urls.GET_USER_ORDERS)
        assert response.status_code == 401 and response.json()['message'] == ResponsesText.GET_ORDERS_WITHOUT_AUTH
