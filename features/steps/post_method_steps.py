from behave import step
from utilities.apifunctions import ApiFunctions
from utilities.asserts_helper import *


@step("user sends POST method to {endpoint} for post a {element}")
def post_element_to(context, endpoint, element):
    context.api = ApiFunctions()
    context.response = context.api.post_request(endpoint, element)


@step("user verifies post status code {code}")
def post_status_code_is(context, code):
    context.api = ApiFunctions()
    assert_status_code(context.api.check_status_code(context.response, code))


@step("user verifies the post response has the correct info for posted {element}")
def check_posted_info(context, element):
    context.api = ApiFunctions()
    assert_data_response(context.api.check_post_returned(element, context.response))


@step("user verifies the post response is empty")
def check_empty_response(context):
    context.api = ApiFunctions()
    assert_data_response(context.api.check_post_returned("empty", context.response))
