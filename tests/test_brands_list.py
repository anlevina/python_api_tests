import allure

from scr.pydantic_schemas.get_brands_list import GetBrandsListResponse
from scr.baseclasses.response_validation import Response
from scr.enums.global_enums import BrandErrorMessages


@allure.title('Check GET brands request')
def test_get_brands_list_success(get_brand_response):

    response = Response(get_brand_response)
    response.assert_status_code(200).assert_response_code(200).validate(GetBrandsListResponse)


@allure.title('Check PUT brand request')
def test_put_brand_failure(put_brand_response):

    response = Response(put_brand_response)
    (response.assert_status_code(200).assert_response_code(405)
     .assert_message(BrandErrorMessages.PUT_BRAND_METHOD_NOT_SUPPORTED.value))



