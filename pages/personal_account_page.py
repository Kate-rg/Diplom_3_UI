from selenium.webdriver.common.by import By
from data import Urls
from pages.base_page import BasePage
import allure


class PersonalAccountPage(BasePage):

    @allure.step('Кликаем по кнопке "Конструктор"')
    def click_button_constructor(self):
        self.click(self.BUTTON_CONSTRUCTOR)

    @allure.step('Кликаем по кнопке "История заказов"')
    def click_history_profile(self):
        self.click(self.BUTTON_HISTORY_PROFILE)

    @allure.step('Кликаем по кнопке "Выход"')
    def click_exit_button(self):
        self.click(self.EXIT_BUTTON)

    @allure.step('Кликаем по кнопке "Личный кабинет"')
    def click_button_personal_account(self):
        self.click(self.BUTTON_ACCOUNT)

    @allure.step('Вводим почту')
    def enter_email(self, email):
        email_input = self.find_element_with_wait(self.INPUT_EMAIL)
        email_input.send_keys(email)

    @allure.step('Вводим пароль')
    def enter_password(self, password):
        email_input = self.find_element_with_wait(self.INPUT_PASSWORD)
        email_input.send_keys(password)

    @allure.step('Кликаем по кнопке "Войти"')
    def click_enter_button(self):
        self.click(self.BUTTON_ENTER)

    @allure.step('Ожидаем смены страницы логина')
    def wait_for_url_changes_login(self):
        self.wait_url_changes(Urls.BASE_PAGE + Urls.LOGIN_PAGE)

    @allure.step('Ожидаем смены главной страницы')
    def wait_for_url_changes_main(self):
        self.wait_url_changes(Urls.BASE_PAGE)

    @allure.step('Ожидаем смены страницы аккаунт')
    def wait_for_url_changes_account(self):
        self.wait_url_changes(Urls.BASE_PAGE + Urls.ACCOUNT_PROFILE_PAGE)

    @allure.step('Ожидаем смены страницы аккаунт-профайл')
    def wait_for_url_changes_profile_account(self):
        self.wait_url_changes(Urls.BASE_PAGE + Urls.ACCOUNT_PROFILE_PAGE_FINAL)

    @allure.step('Входим в личный кабинет с ожиданием смены необходимых страниц')
    def click_enter_personal_account_wait_pages_changes(self):
        self.click_enter_button()
        self.wait_for_url_changes_login()
        self.click_button_personal_account()
        self.wait_for_url_changes_main()
        self.wait_for_url_changes_account()

    @allure.step('Находим текст кнопки "Сохранить"')
    def get_save_button_text(self):
        return self.get_element_text(self.BUTTON_SAVE)

    BUTTON_ACCOUNT = (By.XPATH, "//*[contains(text(), 'Личный Кабинет')]")
    BUTTON_HISTORY_PROFILE = (By.XPATH, "//a[text()='История заказов']")
    BUTTON_SAVE = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
    INPUT_EMAIL = (By.XPATH, "//label[text() = 'Email']/../input")
    INPUT_PASSWORD = (By.XPATH, "//label[text() = 'Пароль']/../input")
    BUTTON_ENTER = (By.XPATH, "//button[text()='Войти']")
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")






