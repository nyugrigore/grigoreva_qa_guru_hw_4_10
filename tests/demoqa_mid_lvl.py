from models.pages import RegistrationPage


def test_demoqa_registration_positive(browser_configs):
    """
    Позитивный тест на регистрацию: все поля
    """
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.fill_1st_name("User")
    registration_page.fill_last_name("Default")
    registration_page.fill_user_email("default@mail.com")

    registration_page.fill_gender("Male")
    registration_page.fill_phone_number("9111111111")
    registration_page.fill_date_of_birth('1991', 'November', '03')
    registration_page.fill_subject("ma")
    registration_page.scroll_down()
    registration_page.fill_hobbies("Sports")
    registration_page.upload_picture("icon.jpg")
    registration_page.fill_address("Saint P Nevskiy prospect 111")
    registration_page.fill_state("NCR")
    registration_page.fill_city("Delhi")

    registration_page.click_submit()

    # THEN
    registration_page.should_have_successful_result()
    registration_page.should_have_registered(
        'User Default',
        'default@mail.com',
        'Male',
        '9111111111',
        '03 November,1991',
        'Maths',
        'Sports',
        'icon.jpg',
        'Saint P Nevskiy prospect 111',
        'NCR Delhi'
    )

    registration_page.close()
