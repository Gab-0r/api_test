from behave import step
from utilities.apifunctions import ApiFunctions


@step("user sends GET method to {endpoint}")
def get_single_element(context, endpoint):
    context.api = ApiFunctions()
    context.response = context.api.get_request(endpoint)


@step("user verifies the response status code is {status_code}")
def check_status_code(context, status_code):
    context.api = ApiFunctions()
    assert context.api.check_status_code(context.response, status_code), "Status code is not the expected"


@step("user verifies the get response has the correct info for {element}")
def check_response_info(context, element):
    context.api = ApiFunctions()
    assert context.api.check_get(context.response, element), "The data returned is wrong"


@step("user verifies the response for get all {name} resources")
def check_response_len(context, name):
    context.api = ApiFunctions()
    assert context.api.check_getall_len(context.response, name), "data is wrong"