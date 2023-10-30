from behave import step
from utilities.apifunctions import ApiFunctions
from utilities.asserts_helper import *

@step("user verifies the status code is {code}")
def check_status_code(context, code):
    context.api = ApiFunctions()
    assert_status_code(context.api.check_status_code(context.response, code))