import os

from selene import browser, have, command


class RegistrationPage:
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
        self.submit = browser.element("#submit")

    def open(self):
        browser.open("https://demoqa.com/automation-practice-form")
        return self

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
        self.photo.send_keys(os.getcwd() + f'/resources/{value}')
        return self

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

    def click_submit(self):
        self.submit.perform(command.js.click)
        return self

    def should_have_successful_result(self):
        browser.element("#example-modal-sizes-title-lg").should(
            have.exact_text("Thanks for submitting the form")
        )
        return self

    def should_have_registered(
        self,
        full_name,
        email,
        gender,
        phone_number,
        date_of_birth,
        subjects,
        hobbies,
        photo,
        address,
        state_city,
    ):
        browser.element(".table").all("td").even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                phone_number,
                date_of_birth,
                subjects,
                hobbies,
                photo,
                address,
                state_city,
            )
        )
        return self

    def close(self):
        browser.element('[id="closeLargeModal"]').perform(command.js.click)
        return self
