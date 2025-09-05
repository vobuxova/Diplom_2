import requests
import allure
from ..data import Urls, Message

@allure.feature("Создание заказа")
class TestOrderCreate:
    
    @allure.title("Создание заказа авторизованным пользователем")
    def test_create_order_by_authorized_user(self,  create_user):
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
        response = requests.post(Urls.ORDER_ENDPOINT, json=payload_ingredients, headers=headers)
        assert response.json()["success"] == True
        assert response.json()["name"] == "Люминесцентный бессмертный метеоритный краторный бургер"
        
        
    @allure.title("Создание заказа неавторизованным пользователем")
    def test_create_order_by_unauthorized_user(self):
        
        payload_ingredients = {
            "ingredients": ["61c0c5a71d1f82001bdaaa6f", "61c0c5a71d1f82001bdaaa70", "61c0c5a71d1f82001bdaaa6e","61c0c5a71d1f82001bdaaa6c"]
            }

        response = requests.post(Urls.ORDER_ENDPOINT, json=payload_ingredients)
        assert response.json()["success"] == True
        assert response.json()["name"] == "Люминесцентный бессмертный метеоритный краторный бургер"
        
        
    @allure.title("Создание заказа авторизованным пользователем без ингридиентов")
    def test_create_order_by_authorized_user_without_ingredients(self,  create_user):
        email, password, _ = create_user
        
        payload = {
            "email": email,
            "password": password
        }
        
        r = requests.post(Urls.LOGIN_ENDPOINT, json=payload)
        token = r.json()["accessToken"]
        payload_ingredients = {
            "ingredients": []
            }

        headers = {"Authorization": token}
        response = requests.post(Urls.ORDER_ENDPOINT, json=payload_ingredients, headers=headers)
        assert response.json()["success"] == False
        assert response.json()["message"] == Message.ingredient_error
        
        
    @allure.title("Создание заказа неавторизованным пользователем без ингридиентов")
    def test_create_order_by_unauthorized_user_without_ingredients(self):
       
        payload_ingredients = {
            "ingredients": []
            }

        response = requests.post(Urls.ORDER_ENDPOINT, json=payload_ingredients)
        assert response.json()["success"] == False
        assert response.json()["message"] == Message.ingredient_error
        
        
    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_with_incorrect_ingredients_ids(self, create_user):
        email, password, _ = create_user
        
        payload = {
            "email": email,
            "password": password
        }
        
        r = requests.post(Urls.LOGIN_ENDPOINT, json=payload)
        token = r.json()["accessToken"]
        payload_ingredients = {
            "ingredients": ["61c0c5a71d1f82001bdaaa6f11", "61c0c5a71d1f82001bdaaa7011", "61c0c5a71d1f82001bdaaa6e111","61c0c5a71d1f82001bdaaa6c11111"]
            }

        headers = {"Authorization": token}
        response = requests.post(Urls.ORDER_ENDPOINT, json=payload_ingredients, headers=headers)
        assert response.status_code == 500
    
    