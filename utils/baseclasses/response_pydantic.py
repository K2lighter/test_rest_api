

class Response_pydantic:

    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code

    def validate_2(self, schema):
        schema.parse_obj(self.response_json)
        return self

    def assert_status_code_2(self, status_code):
        assert self.response_status == status_code
        return self
