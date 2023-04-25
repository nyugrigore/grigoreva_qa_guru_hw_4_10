from selene import browser, have, be, command
import os


def test_demoqa_registration_positive(browser_configs):
    """
    Позитивный тест на регистрацию: все поля
    """
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('User')
    browser.element('#lastName').type('Default')
    browser.element('#userEmail').type('default@mail.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('9111111111')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('option[value="10"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('option[value="1991"]').click()
    browser.element('.react-datepicker__day--003').click()
    browser.element('#subjectsInput').type('ma').press_enter()
    browser.driver.execute_script('window.scrollBy(0, 100)')
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').send_keys(os.getcwd() + 'resources/icon.jpg')
    browser.element('#currentAddress').type('City Saint-P')
    browser.element('#react-select-3-input').should(be.blank).type('Rajasthan').press_enter()
    browser.element('#react-select-4-input').should(be.blank).type('Jaiselmer').press_enter().press_enter()
    # Проверка результатов
    browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
    browser.element('//tbody/tr[1]/td[2]').should(have.text('User Default'))
    browser.element('//tbody/tr[2]/td[2]').should(have.text('default@mail.com'))
    browser.element('//tbody/tr[3]/td[2]').should(have.text('Male'))
    browser.element('//tbody/tr[4]/td[2]').should(have.text('9111111111'))
    browser.element('//tbody/tr[5]/td[2]').should(have.text('03 November,1991'))
    browser.element('//tbody/tr[6]/td[2]').should(have.text('Maths'))
    browser.element('//tbody/tr[7]/td[2]').should(have.text('Sports'))
    browser.element('//tbody/tr[8]/td[2]').should(have.text('icon.jpg'))
    browser.driver.execute_script('window.scrollBy(0, 100)')
    browser.element('//tbody/tr[9]/td[2]').should(have.text('City Saint-P'))
    browser.element('//tbody/tr[10]/td[2]').should(have.text('Rajasthan Jaiselmer'))
    browser.element('[id="closeLargeModal"]').perform(command.js.click)
