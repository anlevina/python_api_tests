from enum import Enum


class GlobalErrorMessages(Enum):

    WRONG_STATUS_CODE = 'Another status code is expected.'
    WRONG_RESPONSE_CODE = 'Another responseCode code is expected in json object.'
    DIFFERENT_JSON_OBJECTS = 'Compared json objects are different.'
    WRONG_MESSAGE = 'Another message is expected.'


class SearchProductErrorMessages(Enum):

    POST_SEARCH_PRODUCT_MISSING_PARAMETER = 'Bad request, search_product parameter is missing in POST request.'


class ProductErrorMessages(Enum):

    POST_PRODUCT_METHOD_NOT_SUPPORTED = 'This request method is not supported.'


class BrandErrorMessages(Enum):

    PUT_BRAND_METHOD_NOT_SUPPORTED = 'This request method is not supported.'


class UserAccountSuccessMessages(Enum):

    CREATE_USER_SUCCESS = 'User created!'
    UPDATE_USER_SUCCESS = 'User updated!'
    DELETE_USER_SUCCESS = 'Account deleted!'


class UserAccountErrorMessages(Enum):

    PUT_ACCOUNT_NOT_FOUND_FAILURE = 'Account not found!'
    POST_NO_EMAIL_USER_FAILURE = 'Bad request, email parameter is missing in POST request.'
    PUT_NO_EMAIL_USER_FAILURE = 'Bad request, email parameter is missing in PUT request.'
    PUT_NO_PASSWORD_USER_FAILURE = 'Bad request, password parameter is missing in PUT request.'


class VerifyLoginSuccessMessages(Enum):

    VERIFY_LOGIN_SUCCESS = 'User exists!'


class VerifyLoginErrorMessages(Enum):

    VERIFY_LOGIN_NO_EMAIL = 'Bad request, email or password parameter is missing in POST request.'
    VERIFY_LOGIN_USER_NOT_FOUND = 'User not found!'
    VERIFY_LOGIN_NO_EMAIL_OR_PASSWORD = 'Bad request, email or password parameter is missing in POST request.'
    VERIFY_LOGIN_METHOD_NOT_SUPPORTED = 'This request method is not supported.'

