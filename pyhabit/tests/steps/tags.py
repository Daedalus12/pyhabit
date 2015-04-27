from behave import *
from pyhabit import hrpg
from unittest import TestCase

tc = TestCase('__init__')

DEFAULT_TAG_KEYS = [
    '0f005e95-3140-4482-b94b-1eaa0e6135d6',
    '2a19221b-a88d-48e5-8f23-4ce5f29868cf',
    'ba3b805d-4eec-42d8-8bd9-77c24c983f0d' ]

use_step_matcher("re")

@when("I ask for current tags")
def step_impl(context):
    context.tags = context.user.getTags()


@then("I should get the default tags")
def step_impl(context):

    tc.assertEquals(len(context.tags), 3)

    for key in DEFAULT_TAG_KEYS:
        tc.assertIn(key, context.tags)


@when("I create a new tag")
def step_impl(context):
    context.newTag = context.user.createTag( 'office' )


@step("I add it")
def step_impl(context):
    context.user.addTag(context.newTag)


@then("The new tag should exist")
def step_impl(context):
    assert( context.newTag.id in context.tags ) 


@step("I modify the tag")
def step_impl(context):
    context.newTag.name = 'work'
    context.user.updateTag( context.newTag )


@then("The modified tag should be different")
def step_impl(context):
    assert( context.tags[context.newTag.id].name == 'work' )


@step("I delete that tag")
def step_impl(context):
    context.user.deleteTag( context.newTag )


@then("The deleted tag should be gone")
def step_impl(context):
    assert( context.newTag.id not in context.tags )
