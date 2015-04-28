from behave import *
from unittest import TestCase

tc = TestCase('__init__')


@when("I create a new todo {text}")
def step_impl(context, text):
    context.task = context.user.createTask( text )


@step("I add the task")
def step_impl(context):
    context.user.addTask( context.task )


@step("I ask for current tasks")
def step_impl(context):
    context.tasks = context.user.getTasks( )


@then("The new task should exist")
def step_impl(context):
    tc.assertIn(context.task.id, context.tasks)


@when("I modify the task")
def step_impl(context):
    context.task.text = 'Fire the sun'
    context.user.updateTask( context.task )

@then("The modified task should be different")
def step_impl(context):
    tc.assertEqual(context.tasks[context.task.id].text, 'Fire the sun')


@when("I perform the task")
def step_impl(context):
    context.user.performTask(context.task)


@then("The task should be completed")
def step_impl(context):
    tc.assertTrue( context.task.completed )


@when("I delete that task")
def step_impl(context):
    context.user.deleteTask( context.task )


@then("The deleted task should be gone")
def step_impl(context):
    tc.assertIsNone(context.task)


@step("I ask for the specific task")
def step_impl(context):
    context.user.getTask( context.task.id )
