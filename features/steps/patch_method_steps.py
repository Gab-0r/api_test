from behave import step
from utilities.apifunctions import ApiFunctions
from utilities.asserts_helper import *


@step("user sends PATCH method to {endpoint} and patch a {element}")
def path_element_at(context, endpoint, element):
    context.api = ApiFunctions()
    context.response = context.api.send_request("PATCH",endpoint, data=element)


@step("user verifies patch status code {code}")
def patch_status_code_is(context, code):
    context.api = ApiFunctions()
    assert_status_code(context.api.check_status_code(context.response, code))


@step("user verifies the patch response has the correct info for patched {element}")
def patch_check_info(context, element):
    context.api = ApiFunctions()
    assert_data_response(context.api.check_patch_returned(context.response, element))


@step("user verifies the PATCH response is empty")
def check_patch_empty_response(context):
    context.api = ApiFunctions()
    assert_data_empty(context.api.check_patch_returned(context.response, "empty"))
