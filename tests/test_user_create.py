import requests
import allure
from ..data import Urls, Message
from ..helpers import Helpers
from ..user_generator import return_email_password_name, delete_user

@allure.feature("Создание пользователя")
class TestCreateUser:
    
    @allure.title("Успешное создание уникального пользователя")
    def test_create_user_with_correct_data(self):
        email = Helpers.generate_email(10)
        password = Helpers.generate_random_string(10)
        name = Helpers.generate_random_string(10)
        
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        
        response = requests.post(Urls.USER_CREATE_ENDPOINT, json=payload)
        
        assert response.json()["success"] == True
        assert response.json()["user"]["email"] == email
        
        delete_user(email, password)
        
        
        
    @allure.title("Cоздание уже существующего пользователя")
    def test_create_existing_user(self, create_user):
        email, password, name = create_user
        
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        
        response = requests.post(Urls.USER_CREATE_ENDPOINT, json=payload)
        
        assert response.json()["success"] == False
        assert response.json()["message"] == Message.user_creation_error
    
    @allure.title("Cоздание пользователя без одного из обязательных полей")
    def test_create_user_missing_field(self):
        _, password, name = return_email_password_name()
        
        payload = {
            "password": password,
            "name": name
        }
        
        response = requests.post(Urls.USER_CREATE_ENDPOINT, json=payload)
        
        assert response.json()["success"] == False
        assert response.json()["message"] == Message.data_create_error
        
        
        
        
        