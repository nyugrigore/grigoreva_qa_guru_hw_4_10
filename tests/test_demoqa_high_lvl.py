from allure_commons.types import Severity

from data.users import def_user
from models.simple_user_registration_page import SimpleRegistrationPage

import allure

@allure.tag("critical")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "nyugrigore")
@allure.feature("Регистрация нового пользователя")
@allure.story("Новый пользователь может зарегистрироваться на сайте https://demoqa.com")
@allure.link("https://demoqa.com/automation-practice-form", name="Registration form")
def test_register_user(browser_configs):
    registration_page = SimpleRegistrationPage()

    with allure.step("Открываем страницу регистрации"):
        registration_page.open()

    with allure.step("Заполняем форму регистрации нового пользователя"):
        registration_page.fill(def_user)

    with allure.step("Подтверждаем заполнение формы регистрации"):
        registration_page.submit()

    with allure.step("Проверяем сохраненные данные пользователя"):
        registration_page.should_have_submited(def_user)
