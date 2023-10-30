from behave import step
from utilities.apifunctions import ApiFunctions
from utilities.asserts_helper import *


@step("user sends GET method to {endpoint}")
def get_single_element(context, endpoint):
    context.api = ApiFunctions()
    context.response = context.api.send_request("GET", endpoint)


@step("user verifies the response status code is {status_code}")
def check_status_code(context, status_code):
    context.api = ApiFunctions()
    assert_status_code(context.api.check_status_code(context.response, status_code))


@step("user verifies the get response has the correct info for {element}")
def check_response_info(context, element):
    context.api = ApiFunctions()
    assert_data_response(context.api.check_get(context.response, element))


@step("user verifies the response for get all {name} resources")
def check_response_len(context, name):
    context.api = ApiFunctions()
    assert_data_response(context.api.check_getall_len(context.response, name))
