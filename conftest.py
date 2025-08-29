import pytest
import requests
from .data import Urls
from .user_generator import return_email_password_name, delete_user

@pytest.fixture
def create_user():
    email, password, name = return_email_password_name()
    payload = {"email": email, "password": password, "name": name}

    requests.post(Urls.USER_CREATE_ENDPOINT, json=payload)
    
    yield email, password, name
    
    login_payload = {"email": email, "password": password}
    requests.post(Urls.LOGIN_ENDPOINT, json=login_payload)
    delete_user(email, password)
    

    