from selenium.webdriver.common.by import By
from data import Items
from data import Urls
from pages.base_page import BasePage
import allure


class ResetPasswordPage(BasePage):

    @allure.step('Кликаем по кнопке "Входа в аккаунт"')
    def click_button_enter_account(self):
        self.click(self.BUTTON_ENTER_ACCOUNT)

    @allure.step('Кликаем по кнопке "Восстановить пароль')
    def click_reset_password(self):
        self.click(self.BUTTON_RESET_PASSWORD)

    @allure.step('Кликаем по кнопке "Входа в аккаунт" и "Восстановить пароль"')
    def enter_and_click_reset_password(self):
        self.click_button_enter_account()
        self.click_reset_password()

    @allure.step('Вводим почту')
    def set_email_input(self, email):
        email_input = self.find_element_with_wait(self.EMAIL_FIELD)
        email_input.send_keys(email)

    @allure.step('Кликаем по кнопке "Восстановить"')
    def click_button_restore_password(self):
        self.click(self.RESTORE_BUTTON)

    @allure.step('Вводим почту и кликаем по кнопке "Восстановить"')
    def set_email_and_click_restore_button(self):
        self.set_email_input(Items.email)
        self.click_button_restore_password()

    @allure.step('Ожидаем смены веб-странички с восстановлением пароля')
    def wait_for_url_changes_restore(self):
        self.wait_url_changes(Urls.BASE_PAGE + Urls.FORGOT_PASSWORD_PAGE)

    @allure.step('Проверяем что тип поля ввода пароля - текст')
    def get_input_password_status(self):
        input_status = self.find_element_with_wait(self.PASSWORD_FIELD)
        return input_status.get_attribute("type") == 'text'

    @allure.step('Кликаем по "показать пароль" в поле ввода пароля')
    def click_eye(self):
        self.click(self.CLICK_AYE_AREA)

    BUTTON_ENTER_ACCOUNT = (By.XPATH, "//button[text()='Войти в аккаунт']")
    BUTTON_RESET_PASSWORD = (By.XPATH, "//*[contains(@href,'/forgot-password')]")
    EMAIL_FIELD = (By.XPATH, "//input[@class='text input__textfield text_type_main-default']")
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='Введите новый пароль']")
    CLICK_AYE_AREA = (By.XPATH, "//div[@class='input__icon input__icon-action']")




