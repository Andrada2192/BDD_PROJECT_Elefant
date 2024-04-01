from behave import *


@given('I am on the main page')
def step_impl(context):
    context.TestSearchBar.navigate_to_login_page()


@when('I enter "{item}" in search field')
def step_impl(context, item):
    context.TestSearchBar.search_bar_field(item)


@when('I press the search button')
def step_impl(context):
    context.TestSearchBar.click_search_button()


@then('I should see a list of elements with less than 10 items')
def step_impl(context):
    products = context.TestSearchBar.product_list()
    assert len(products) < 10


@then('I should see an error message')
def step_impl(context):
    actual_error_message = context.TestSearchBar.get_error_message()
    expected_error_message = 'NU A FOST GĂSIT NICI UN REZULTAT :'
    assert expected_error_message in actual_error_message