import allure
import pytest

from scr.pydantic_schemas.get_search_product import GetSearchProductResponse
from scr.baseclasses.response_validation import Response
from scr.enums.global_enums import SearchProductErrorMessages
from scr.test_data.test_data_search_product import SearchProduct


@allure.title('Positive test for POST search product')
@pytest.mark.parametrize("form_data", [
    SearchProduct.search_product,
    SearchProduct.search_product_two_parameters,
    SearchProduct.search_product_empty_parameter,
    SearchProduct.search_product_one_wrong_parameter,
    SearchProduct.search_product_empty_list
])
def test_post_search_product_success(post_search_product_response, form_data):
    post_response = Response(post_search_product_response)
    (post_response.assert_status_code(200).assert_response_code(200)
     .validate(GetSearchProductResponse))


@allure.title('Negative test for POST search product')
@pytest.mark.parametrize("form_data", [
    SearchProduct.search_product_wrong_parameter_name,
    SearchProduct.search_product_empty_data
])
def test_post_search_product_failure(post_search_product_response, form_data):
    post_response = Response(post_search_product_response)
    (post_response.assert_status_code(200).assert_response_code(400)
     .assert_message(SearchProductErrorMessages.POST_SEARCH_PRODUCT_MISSING_PARAMETER.value))

