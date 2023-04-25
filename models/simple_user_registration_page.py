import os

from selene import browser, have, command

import tests
from data.users import User


class SimpleRegistrationPage:
    def __init__(self):
        self.first_name = browser.element("#firstName")
        self.last_name = browser.element("#lastName")
        self.user_email = browser.element("#userEmail")
        self.gender = browser.all("[name=gender]")
        self.phone_number = browser.element("#userNumber")
        self.date_of_birth_input = browser.element("#dateOfBirthInput")
        self.month_of_birth = browser.element(".react-datepicker__month-select")
        self.year_of_birth = browser.element(".react-datepicker__year-select")
        self.subject = browser.element("#subjectsInput")
        self.hobbies = browser.all(".custom-checkbox")
        self.photo = browser.element("#uploadPicture")
        self.address = browser.element("#currentAddress")
        self.state = browser.element("#state")
        self.list_state = browser.all("[id^=react-select][id*=option]")
        self.city = browser.element("#city")
        self.list_city = browser.all("[id^=react-select][id*=option]")
        self.submit_click = browser.element("#submit")

    def open(self):
        browser.open('/automation-practice-form')
        browser.driver.execute_script("window.scrollBy(0, 100)")

    def fill_1st_name(self, value):
        self.first_name.type(value)
        return self

    def fill_last_name(self, value):
        self.last_name.type(value)
        return self

    def fill_user_email(self, value):
        self.user_email.type(value)
        return self

    def fill_gender(self, value):
        self.gender.element_by(have.value(value)).element("..").click()
        return self

    def fill_phone_number(self, value):
        self.phone_number.type(value)
        return self

    def fill_subject(self, value):
        self.subject.type(value).press_enter()
        return self

    def fill_hobbies(self, value):
        self.hobbies.element_by(have.exact_text(value)).click()
        return self

    def fill_address(self, value):
        self.address.type(value)
        return self

    def fill_city(self, value):
        self.city.click()
        self.list_city.element_by(have.exact_text(value)).click()
        return self

    def fill_state(self, value):
        self.state.perform(command.js.scroll_into_view)
        self.state.click()
        self.list_state.element_by(have.exact_text(value)).click()
        return self

    def upload_picture(self, value):
        self.photo.send_keys(
            os.path.abspath(
                os.path.join(os.path.dirname(tests.__file__), f"resources/{value}")
            )
        )

    def fill_date_of_birth(self, year, month, day):
        self.date_of_birth_input.click()
        self.month_of_birth.type(month)
        self.year_of_birth.type(year)
        browser.element(
            f".react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)"
        ).click()
        return self

    def scroll_down(self):
        browser.driver.execute_script("window.scrollBy(0, 100)")

    def submit(self):
        self.submit_click.perform(command.js.click)

    def close(self):
        browser.element('[id="closeLargeModal"]').perform(command.js.click)
        return self

    def fill(self, def_user: User):
        self.fill_1st_name(def_user.first_name)
        self.fill_last_name(def_user.last_name)
        self.fill_user_email(def_user.email)
        self.fill_gender(def_user.gender)
        self.fill_phone_number(def_user.phone_number)
        self.fill_date_of_birth(def_user.birth_year, def_user.birth_month, def_user.birth_day)
        self.fill_subject(def_user.subjects)
        self.scroll_down()
        self.fill_hobbies(def_user.hobbies)
        self.upload_picture(def_user.photo)
        self.fill_address(def_user.address)
        self.fill_state(def_user.state)
        self.fill_city(def_user.city)

    def should_have_submited(self, def_user: User):
        browser.element(".table").all("td").even.should(
            have.exact_texts(
                def_user.full_name,
                def_user.email,
                def_user.gender,
                def_user.phone_number,
                def_user.date_of_birth,
                def_user.subjects,
                def_user.hobbies,
                def_user.photo,
                def_user.address,
                def_user.state_city,
            )
        )
