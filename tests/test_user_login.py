import requests
import allure
from ..data import Urls, Message
from ..user_generator import delete_user

@allure.feature("Aвторизация пользователя")
class TestLoginUser:
    @allure.title("Успешная авторизация существующего пользователя")
    def test_login_user_with_correct_data(self, create_user):
        email, password, _ = create_user
        
        payload = {
            "email": email,
            "password": password
        }
        
        response = requests.post(Urls.LOGIN_ENDPOINT, json=payload)
        
        assert response.json()["success"] == True
        assert response.json()["user"]["email"] == email
        delete_user(email, password)
        
          
    @allure.title("Авторизация пользователя с несуществующими email и password")
    def test_login_existing_user(self):
        
        payload = {
            "email": "test_user@sdhfgsd.ru",
            "password": "password"
        }
        response = requests.post(Urls.LOGIN_ENDPOINT, json=payload)
        
        assert response.status_code == 401
        assert response.json()["success"] == False
        assert response.json()["message"] == Message.data_incorrect_error
    
    
    @allure.title("Авторизация пользователя при незаполненном обязательном поле")
    def test_login_user_missing_field(self, create_user):
        email, _, _ = create_user
        
        payload_login = {
            "email": email
        }
        response = requests.post(Urls.LOGIN_ENDPOINT, json=payload_login)
        
        assert response.status_code == 401
        assert response.json()["success"] == False
        assert response.json()["message"] == Message.data_incorrect_error
        