import allure

from scr.pydantic_schemas.get_products_list import GetProductsListResponse
from scr.baseclasses.response_validation import Response
from scr.enums.global_enums import ProductErrorMessages


@allure.title('Check GET products list request')
def test_get_products_list_success(get_product_response):

    response = Response(get_product_response)
    response.assert_status_code(200).assert_response_code(200).validate(GetProductsListResponse)


@allure.title('Check POST product request')
def test_post_product_failure(post_product_response):

    response = Response(post_product_response)
    (response.assert_status_code(200).assert_response_code(405)
     .assert_message(ProductErrorMessages.POST_PRODUCT_METHOD_NOT_SUPPORTED.value))



