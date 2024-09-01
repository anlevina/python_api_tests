import allure
import pytest

from scr.baseclasses.response_validation import Response
from scr.enums.global_enums import VerifyLoginSuccessMessages, VerifyLoginErrorMessages
from scr.test_data.test_data_users import Users


@allure.title('Positive test - verify login')
@pytest.mark.parametrize("user_data, verification_data", [
    (Users.extended_user_data, Users.basic_user_data)
])
def test_verify_login_success(post_user_account_response, post_verify_login_response, user_data, verification_data):
    response = Response(post_verify_login_response)
    (response.assert_response_code(200).assert_status_code(200)
     .assert_message(VerifyLoginSuccessMessages.VERIFY_LOGIN_SUCCESS.value))


@allure.title('Negative test - verify login, incomplete data')
@pytest.mark.parametrize("verification_data", [
    Users.email_only_user_data,
    Users.password_only_user_data,
    Users.no_email_user_data
])
def test_verify_login_incomplete_data_failure(post_verify_login_response, verification_data):
    response = Response(post_verify_login_response)
    (response.assert_response_code(400).assert_status_code(200)
     .assert_message(VerifyLoginErrorMessages.VERIFY_LOGIN_NO_EMAIL_OR_PASSWORD.value))


@allure.title('Negative test - verify login, invalid data')
@pytest.mark.parametrize("verification_data", [
    Users.invalid_basic_user_data
])
def test_verify_login_invalid_data_failure(post_verify_login_response, verification_data):
    response = Response(post_verify_login_response)
    (response.assert_response_code(404).assert_status_code(200)
     .assert_message(VerifyLoginErrorMessages.VERIFY_LOGIN_USER_NOT_FOUND.value))


@allure.title('Check DELETE verify login')
def test_delete_verify_login_failure(delete_verify_login_response):
    response = Response(delete_verify_login_response)
    (response.assert_response_code(405).assert_status_code(200)
     .assert_message(VerifyLoginErrorMessages.VERIFY_LOGIN_METHOD_NOT_SUPPORTED.value))


