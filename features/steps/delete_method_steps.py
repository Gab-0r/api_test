from behave import step
from utilities.apifunctions import ApiFunctions
from utilities.asserts_helper import *


@step("user sends DELETE method to {endpoint} for delete a {element}")
def delete_resource_at(context, endpoint, element):
    context.api = ApiFunctions()
    context.response = context.api.send_request("DELETE",endpoint)


@step("user verifies the DELETE response is empty")
def check_delete_response(context):
    context.api = ApiFunctions()
    assert_data_empty(context.api.check_delete_return(context.response))
