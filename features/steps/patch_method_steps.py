from behave import step
from utilities.apifunctions import ApiFunctions


@step("user sends PATCH method to {endpoint} and patch a {element}")
def path_element_at(context, endpoint, element):
    context.api = ApiFunctions()
    context.response = context.api.patch_request(endpoint, element)


@step("user verifies patch status code {code}")
def patch_status_code_is(context, code):
    context.api = ApiFunctions()
    assert context.api.check_status_code(context.response, code), "status code is not expected"


@step("user verifies the patch response has the correct info for patched {element}")
def patch_check_info(context, element):
    context.api = ApiFunctions()
    assert context.api.check_patch_returned(context.response, element)