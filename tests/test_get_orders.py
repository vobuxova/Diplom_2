import requests
import allure
from ..data import Urls, Message

@allure.feature("Получение заказов")
class TestGetOrders:
    
    @allure.title("Получение заказов авторизованного пользователя")
    def test_get_orders_authirozed_user(self, create_user):
        email, password, _ = create_user
        
        payload = {
            "email": email,
            "password": password
        }
        
        r = requests.post(Urls.LOGIN_ENDPOINT, json=payload)
        token = r.json()["accessToken"]
        payload_ingredients = {
            "ingredients": ["61c0c5a71d1f82001bdaaa6f", "61c0c5a71d1f82001bdaaa70", "61c0c5a71d1f82001bdaaa6e","61c0c5a71d1f82001bdaaa6c"]
            }

        headers = {"Authorization": token}
        requests.post(Urls.ORDER_ENDPOINT, json=payload_ingredients, headers=headers)
        orders_response = requests.get(Urls.ORDER_ENDPOINT, headers=headers)
        assert orders_response.json()["success"] == True
        assert orders_response.json()["orders"][0]["ingredients"] == ["61c0c5a71d1f82001bdaaa6f", "61c0c5a71d1f82001bdaaa70", "61c0c5a71d1f82001bdaaa6e","61c0c5a71d1f82001bdaaa6c"]
        
        
    @allure.title("Получение заказов неавторизованного пользователя")
    def test_get_orders_unauthirozed_user(self):

        orders_response = requests.get(Urls.ORDER_ENDPOINT)
        assert orders_response.status_code == 401
        assert orders_response.json()["success"] == False
        assert orders_response.json()["message"] == Message.unauthorized_error