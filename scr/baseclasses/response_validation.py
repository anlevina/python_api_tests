import allure

from scr.enums.global_enums import GlobalErrorMessages


class Response:

    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code

    @allure.step('Validate json from response')
    def validate(self, schema):
        """
        This method validates json object from a response with a pydantic schema.
        """
        schema.model_validate(self.response_json)
        return self

    @allure.step('Check status code of response')
    def assert_status_code(self, status_code):
        """
        This method validates HTTP request response code.
        """
        assert self.response_status == status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        return self

    @allure.step('Check response code from response body')
    def assert_response_code(self, response_code):
        """
        This method validates responseCode object from response body.
        """
        assert self.response_json['responseCode'] == response_code, GlobalErrorMessages.WRONG_RESPONSE_CODE.value
        return self

    @allure.step('Check message from response body')
    def assert_message(self, message):
        """
        This method validates message object from response body.
        """
        assert self.response_json['message'] == message, GlobalErrorMessages.WRONG_MESSAGE.value
        return self
