import pytest
import requests

from scr.test_data.test_data_users import Users
from scr.api.urls import (BASE_URL, PRODUCTS_LIST_ENDPOINT, BRANDS_LIST_ENDPOINT, CREATE_ACCOUNT_ENDPOINT,
                          DELETE_USER_DETAIL_ENDPOINT, SEARCH_PRODUCT_ENDPOINT, UPDATE_USER_DETAIL_ENDPOINT,
                          VERIFY_LOGIN_ENDPOINT)


@pytest.fixture()
def get_product_response():
    try:
        response = requests.get(url=f'{BASE_URL}/{PRODUCTS_LIST_ENDPOINT}')
        response.raise_for_status()
        print(f'Get product response: {response.json()}')
        return response

    except requests.exceptions.RequestException as e:
        pytest.fail(f"Request failed: {e}")


@pytest.fixture()
def post_product_response():
    try:
        response = requests.post(url=f'{BASE_URL}/{PRODUCTS_LIST_ENDPOINT}')
        response.raise_for_status()
        print(f'Create product response: {response.json()}')
        return response

    except requests.exceptions.RequestException as e:
        pytest.fail(f"Request failed: {e}")


@pytest.fixture()
def get_brand_response():
    try:
        response = requests.get(url=f'{BASE_URL}/{BRANDS_LIST_ENDPOINT}')
        response.raise_for_status()
        print(f'Get brand response: {response.json()}')
        return response

    except requests.exceptions.RequestException as e:
        pytest.fail(f"Request failed: {e}")


@pytest.fixture()
def put_brand_response():
    try:
        response = requests.put(url=f'{BASE_URL}/{BRANDS_LIST_ENDPOINT}')
        response.raise_for_status()
        print(f'Update brand response: {response.json()}')
        return response

    except requests.exceptions.RequestException as e:
        pytest.fail(f"Request failed: {e}")


@pytest.fixture()
def post_search_product_response(form_data):
    try:
        response = requests.post(url=f'{BASE_URL}/{SEARCH_PRODUCT_ENDPOINT}', data=form_data)
        response.raise_for_status()
        print(response.json())
        return response

    except requests.exceptions.RequestException as e:
        pytest.fail(f"Request failed: {e}")


@pytest.fixture()
def post_user_account_response(user_data):
    try:
        post_response = requests.post(url=f'{BASE_URL}/{CREATE_ACCOUNT_ENDPOINT}', data=user_data)
        post_response.raise_for_status()
        print(f'Create user response: {post_response.json()}')

        yield post_response
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Request failed: {e}")
        yield None

    finally:
        delete_response = requests.delete(f'{BASE_URL}/{DELETE_USER_DETAIL_ENDPOINT}', data=Users.basic_user_data)
        print(f'Delete user response: {delete_response.json()}')


@pytest.fixture()
def put_user_account_response(changed_user_data):
    try:
        put_response = requests.put(url=f'{BASE_URL}/{UPDATE_USER_DETAIL_ENDPOINT}', data=changed_user_data)
        put_response.raise_for_status()
        print(f'Update user response: {put_response.json()}')
        return put_response

    except requests.exceptions.RequestException as e:
        pytest.fail(f"Request failed: {e}")


@pytest.fixture()
def post_verify_login_response(verification_data):
    try:
        post_response = requests.post(url=f'{BASE_URL}/{VERIFY_LOGIN_ENDPOINT}', data=verification_data)
        post_response.raise_for_status()
        print(f'Verify user response: {post_response.json()}')
        return post_response

    except requests.exceptions.RequestException as e:
        pytest.fail(f"Request failed: {e}")


@pytest.fixture()
def delete_verify_login_response():
    try:
        delete_response = requests.delete(url=f'{BASE_URL}/{VERIFY_LOGIN_ENDPOINT}')
        delete_response.raise_for_status()
        print(f'Delete verify user response: {delete_response.json()}')
        return delete_response
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Request failed: {e}")
