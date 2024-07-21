from pathlib import Path
from selene import browser, have


class StudentRegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')

    def type_first_name(self, first_name):
        browser.element('#firstName').type(first_name)

    def type_last_name(self, last_name):
        browser.element('#lastName').type(last_name)

    def type_email(self, mail):
        browser.element('#userEmail').type(mail)

    def select_gender(self, gender):
        browser.all('[name=gender]').element_by(have.value(gender)).element('..').click()

    def type_user_number(self, user_number):
        browser.element('#userNumber').type(user_number)

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').type(year).click()
        browser.element('.react-datepicker__month-select').type(month).click()
        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()

    def type_subject(self, subject):
        browser.element('#subjectsInput').type(subject).press_enter()

    def type_hobbies(self, hobby1, hobby2):
        browser.all('.custom-checkbox').element_by(have.exact_text(hobby1)).click()
        browser.all('.custom-checkbox').element_by(have.exact_text(hobby2)).click()

    def upload_photo(self, photo):
        browser.element('#uploadPicture').send_keys(str(Path(__file__).parent.parent.joinpath(f'resources/{photo}')))

    def type_address(self, address):
        browser.element('#currentAddress').type(address)

    def type_state(self, state):
        browser.element('#react-select-3-input').type(state).press_enter()

    def type_city(self, city):
        browser.element('#react-select-4-input').type(city).press_enter()

    def element_submit_registration_form(self):
        browser.element('#submit').click()

    def should_have_registered_user_with(self, full_name, mail, gender, user_number, date_of_birth, subject, hobby,
                                         photo, address, state_city):
        browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                mail,
                gender,
                user_number,
                date_of_birth,
                subject,
                hobby,
                photo,
                address,
                state_city
            )
        )
