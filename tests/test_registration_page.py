from allure_commons.types import Severity
from pages.form_page import StudentRegistrationPage
import allure


@allure.tag('registration_form')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Annette-F')
@allure.feature('Полная форма регистрация нового студента')
@allure.story('Регистрация нового студента')
@allure.link('https://demoqa.com/automation-practice-form', name='Demoqa')
def test_student_registration_form():
    with allure.step('Открываем форму регистрации студента'):
        registration_page = StudentRegistrationPage()
        registration_page.open()

    # WHEN
    with allure.step('Заполняем поле ввода First Name'):
        registration_page.type_first_name('Anna')

    with allure.step('Заполняем поле ввода Last Name'):
        registration_page.type_last_name('Fedorova')

    with allure.step('Заполняем поле ввода Email'):
        registration_page.type_email('email@mail.com')

    with allure.step('Отмечаем радио-баттон Gender'):
        registration_page.select_gender('Female')

    with allure.step('Заполняем поле ввода Mobile Number'):
        registration_page.type_user_number('9001234567')

    with allure.step('Указываем дату рождения'):
        registration_page.fill_date_of_birth('1982', 'March', '18')

    with allure.step('Заполняем поле ввода Subjects'):
        registration_page.type_subject('Computer Science')

    with allure.step('Отмечаем чекбокс Hobbies'):
        registration_page.type_hobbies('Sports', 'Reading')

    with allure.step('Загружаем фото'):
        registration_page.upload_photo('photo.png')

    with allure.step('Заполняем поле ввода Current Address'):
        registration_page.type_address('Saint-Petersburg, 190000')

    with allure.step('Выбираем из выпадающего списка штат'):
        registration_page.type_state('NCR')

    with allure.step('Выбираем из выпадающего списка город'):
        registration_page.type_city('Delhi')

    with allure.step('Подтверждаем заполнение формы регистрации'):
        registration_page.element_submit_registration_form()

    # THEN
    with allure.step('Проверяем заполнение формы регистрации'):
        registration_page.should_have_registered_user_with(
            'Anna Fedorova',
            'email@mail.com',
            'Female',
            '9001234567',
            '18 March,1982',
            'Computer Science',
            'Sports, Reading',
            'photo.png',
            'Saint-Petersburg, 190000',
            'NCR Delhi'
        )
