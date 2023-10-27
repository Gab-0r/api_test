from behave import step
from utilities.apifunctions import ApiFunctions


@step("user sends PUT method to {endpoint} for post a {element}")
def put_element_at(context, endpoint, element):
    context.api = ApiFunctions()
    context.response = context.api.put_request(endpoint, element)


@step("user verifies put status code {code}")
def check_put_status(context, code):
    context.api = ApiFunctions()
    assert context.api.check_status_code(context.response, code), "status code is not expected"


@step("user verifies the put response has the correct info for the {element} updated")
def check_put_response(context, element):
    context.api = ApiFunctions()
    assert context.api.check_updated_info(element, context.response)