from behave import *
from pyhabit import hrpg

use_step_matcher("re")

@when("I ask for current tags")
def step_impl(context):
    context.tags = context.user.getTags()


@then("I should get the default tags")
def step_impl(context):
    assert(False)


@when("I create a new tag")
def step_impl(context):
    context.newTag = context.user.createTag( '@office' )


@step("I add it")
def step_impl(context):
    context.user.addTag(context.newTag)


@then("The new tag should exist")
def step_impl(context):
    assert( context.newTag.id in context.tags ) 


@step("I modify the tag")
def step_impl(context):
    context.newTag.name = '@work'


@then("The modified tag should be different")
def step_impl(context):
    assert( context.tags[context.newTag.id].name == '@work' )


@step("I delete that tag")
def step_impl(context):
    context.user.deleteTag( context.newTag.id )


@then("The deleted tag should be gone")
def step_impl(context):
    assert( context.newTag.id not in context.tags )
