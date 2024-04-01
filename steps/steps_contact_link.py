from behave import *


@given('I am on contact page')
def step_impl(context):
    context.ContactLink.navigate_to_contact_page()


@when('I enter "{order_number}" in order number field')
def step_impl(context, order_number):
    context.ContactLink.enter_order_number(order_number)


@when('I enter "{description}" in contact description field')
def step_impl(context, description):
    context.ContactLink.enter_contact_description(description)


@when('I click on upload files button')
def step_impl(context):
    context.ContactLink.click_on_upload_files()


@when('I click on submit button')
def step_impl(context):
    context.ContactLink.click_on_submit_button()


@then('I should see "{message1}", "{message2}" and "{message3}" error messages')
def step_impl(context, message1, message2, message3):
    list_error_elements = context.ContactLink.get_error_messages()

    list_error_messages = []
    for element in list_error_elements:
        list_error_messages.append(element.get_attribute('error_message'))
        return list_error_messages

    assert message1 in list_error_messages, f'{message1} is not in {list_error_messages}'
    assert message2 in list_error_messages, f'{message2} is not in {list_error_messages}'
    assert message3 in list_error_messages, f'{message3} is not in {list_error_messages}'
