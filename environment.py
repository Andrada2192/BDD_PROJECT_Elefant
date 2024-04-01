from browser import Browser
from pages.contact_link import ContactLink
from pages.search_bar import TestSearchBar


def before_all(context):
    context.browser = Browser()
    context.TestSearchBar = TestSearchBar()
    context.ContactLink = ContactLink()

def after_all(context):
    context.browser.close()


