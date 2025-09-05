import requests
import allure
from ..data import Urls, Message
from ..helpers import Helpers

@allure.feature("Изменение данных пользователя")
class TestChangeData:
    
    @allure.title("Изменение данных авторизованного пользователя")
    def test_change_data_authirozed_user(self, create_user):
        email, password, _ = create_user
        
        payload = {
            "email": email,
            "password": password
        }
        
        response = requests.post(Urls.LOGIN_ENDPOINT, json=payload)
        token = response.json()["accessToken"]
        email = Helpers.generate_email(10)
        payload_change = {
            "email": email
        }
        headers = {"Authorization": token}
        change_response = requests.patch(Urls.USER_ENDPOINT, json=payload_change, headers=headers)
        assert change_response.json()["success"] == True
        assert change_response.json()["user"]["email"] == email
        
        
    @allure.title("Изменение данных неавторизованного пользователя")
    def test_change_data_unauthorized_user(self):
        
        email = Helpers.generate_email(10)
        payload_change = {
            "email": email
        }
        change_response = requests.patch(Urls.USER_ENDPOINT, json=payload_change)
        assert change_response.json()["success"] == False
        assert change_response.json()["message"] == Message.unauthorized_error 
        
        