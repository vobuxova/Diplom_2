class Urls:
    BASE_URL = "https://stellarburgers.nomoreparties.site/api"
    ORDER_ENDPOINT = f"{BASE_URL}/orders"
    USER_CREATE_ENDPOINT = f"{BASE_URL}/auth/register"
    LOGIN_ENDPOINT = f"{BASE_URL}/auth/login"
    USER_ENDPOINT = f"{BASE_URL}/auth/user"
    
class Message:
    ingredient_error = "Ingredient ids must be provided"
    reset_email_message = "Reset email sent"
    reset_password_message = "Password successfully reset"
    user_creation_error = "User already exists"
    data_create_error = "Email, password and name are required fields" 
    data_incorrect_error = "email or password are incorrect"
    success_logout_message =  "Successful logout"
    unauthorized_error = "You should be authorised"
    forbidden_error = "User with such email already exists"
    
    