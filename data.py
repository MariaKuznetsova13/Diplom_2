class Urls:
    BASE_URL = 'https://stellarburgers.nomoreparties.site'
    REGISTER_NEW_USER = BASE_URL + '/api/auth/register'
    LOGIN_USER = BASE_URL + '/api/auth/login'
    LOGOUT_USER = BASE_URL + '/api/auth/logout '
    GET_USER_DATA = BASE_URL + '/api/auth/user'
    CHANGE_USER_DATA = BASE_URL + '/api/auth/user'
    DELETE_USER = BASE_URL + '/api/auth/user'
    GET_USER_ORDERS = BASE_URL + '/api/orders'
    CREATE_ORDER = BASE_URL + '/api/orders'
    GET_INGREDIENTS = BASE_URL + '/api/ingredients'
    GET_ORDERS = BASE_URL + '/api/orders'


class ResponsesText:
    REGISTER_USER_WITHOUT_REQUIRED_FIELD = 'Email, password and name are required fields'
    LOGIN_WITH_WRONG_PASSWORD_OR_EMAIL = 'email or password are incorrect'
    CHANGE_USER_WITHOUT_AUTH = 'You should be authorised'
    CREATE_ORDER_WITHOUT_INGREDIENTS = 'Ingredient ids must be provided'
    GET_ORDERS_WITHOUT_AUTH = 'You should be authorised'
