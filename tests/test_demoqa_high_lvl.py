from data.users import def_user
from models.simple_user_registration_page import SimpleRegistrationPage


def test_register_user(browser_configs):
    registration_page = SimpleRegistrationPage()

    registration_page.open()
    registration_page.fill(def_user)
    registration_page.submit()

    registration_page.should_have_submited(def_user)
