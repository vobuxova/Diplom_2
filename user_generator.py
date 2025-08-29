import requests
import allure
from .data import Urls
from .helpers import Helpers

@allure.step("Создание данных для регистрации и логина пользователя")
def return_email_password_name():
    
    email = Helpers.generate_email(10)
    password = Helpers.generate_random_string(10)
    name = Helpers.generate_random_string(10)
    return email, password, name

@allure.step("Удаление созданного пользователя")
def delete_user(email, password):
    login_payload = {"email": email, "password": password}
    requests.post(Urls.LOGIN_ENDPOINT, json=login_payload)
    response = requests.delete(f'{Urls.USER_ENDPOINT}')
    return response