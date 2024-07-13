import requests
import pytest

from scr.api.urls import (BASE_URL, GET_USER_DETAIL_ENDPOINT)
from scr.test_data.test_data_users import Users
from scr.pydantic_schemas.get_user_account import GetUserDetailResponse
from scr.baseclasses.response_validation import Response
from scr.enums.global_enums import UserAccountSuccessMessages, UserAccountErrorMessages


def get_user_details_by_email(email):
    get_user_details_response = requests.get(url=f'{BASE_URL}/{GET_USER_DETAIL_ENDPOINT}', params=email)
    return get_user_details_response


@pytest.mark.parametrize("user_data", [
    Users.extended_user_data,
    Users.empty_parameters_user_data
])
def test_create_user_account_success(post_user_account_response, user_data):
    response = Response(post_user_account_response)
    (response.assert_response_code(201).assert_status_code(200)
     .assert_message(UserAccountSuccessMessages.CREATE_USER_SUCCESS.value))


@pytest.mark.parametrize("user_data", [
    Users.no_email_user_data
])
def test_create_user_account_no_email_failure(post_user_account_response, user_data):
    response = Response(post_user_account_response)
    (response.assert_response_code(400).assert_status_code(200)
     .assert_message(UserAccountErrorMessages.POST_NO_EMAIL_USER_FAILURE.value))


@pytest.mark.parametrize("user_data, changed_user_data, data_object, expected_value", [
    (Users.extended_user_data, Users.changed_user_data, 'name', 'Changes')
])
def test_update_user_account_success(post_user_account_response, put_user_account_response,
                                     user_data, changed_user_data, data_object, expected_value):

    response = Response(put_user_account_response)
    (response.assert_response_code(200).assert_status_code(200)
     .assert_message(UserAccountSuccessMessages.UPDATE_USER_SUCCESS.value))

    get_user_details_response = get_user_details_by_email(Users.email_only_user_data)
    get_response = Response(get_user_details_response)
    get_response.assert_response_code(200).assert_status_code(200).validate(GetUserDetailResponse)

    print(f'Check updated user: {get_user_details_response.json()}')
    assert get_user_details_response.json()['user'][data_object] == expected_value


@pytest.mark.parametrize("changed_user_data, response_code, message", [
    (Users.invalid_basic_user_data, 404, UserAccountErrorMessages.PUT_ACCOUNT_NOT_FOUND_FAILURE.value),
    (Users.no_email_user_data, 400, UserAccountErrorMessages.PUT_NO_EMAIL_USER_FAILURE.value),
    (Users.no_password_user_data, 400, UserAccountErrorMessages.PUT_NO_PASSWORD_USER_FAILURE.value)
])
def test_update_user_account_invalid_data_failure(put_user_account_response,
                                                  changed_user_data, response_code, message):

    response = Response(put_user_account_response)
    (response.assert_response_code(response_code).assert_status_code(200)
     .assert_message(message))



