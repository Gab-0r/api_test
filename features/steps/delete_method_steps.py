from behave import step
from utilities.apifunctions import ApiFunctions
from utilities.asserts_helper import *


@step("user sends DELETE method to {endpoint} for delete a {element}")
def delete_resource_at(context, endpoint, element):
    context.api = ApiFunctions()
    context.response = context.api.delete_request(endpoint)


@step("user verifies delete status code {code}")
def delete_status_code(context, code):
    context.api = ApiFunctions()
    assert_status_code(context.api.check_status_code(context.response, code))


@step("user verifies the delete response has the correct info for the resource deleted")
def check_delete_response(context):
    context.api = ApiFunctions()
    assert_data_empty(context.api.check_delete_return(context.response))
