from behave import *
from pyhabit import hrpg

use_step_matcher("re")

@given("I just reset my account")
def step_impl(context):
    context.user = hrpg.User('0ae9d6b0-c729-4533-bfe1-ac22209eb93e',
                             'd3edcc7c-27b9-435d-91a0-e19706430413')
    context.user.reset( )