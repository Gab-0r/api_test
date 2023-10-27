def assert_status_code(response):
    assert response, "status code is not the expected"


def assert_data_response(response):
    assert response, "the body returned is wrong"


def assert_data_empty(response):
    assert response, "the body of the response is not empty"
