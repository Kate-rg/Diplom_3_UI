import allure

from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage
from data import Urls


class TestPersonalAccount:
    @allure.title('Вход в личный кабинет зарегистрированным пользователем')
    @allure.description('Создаем и регистрируем пользователя, логинимся им и входим в его личный кабинет')
    def test_enter_personal_account(self, user, driver):
        email = user["email"]
        password = user["password"]

        page = PersonalAccountPage(driver)
        page.click_button_personal_account()
        page.enter_email(email)
        page.enter_password(password)
        page.click_enter_personal_account_wait_pages_changes()

        assert page.get_save_button_text() == 'Сохранить'


    @allure.title('Проверка оформления заказа авторизованным пользователем')
    @allure.description('Проверяем, что авторизованный пользователь может добавить в корзину ингредиент и оформить заказ')
    def test_make_order_confirmed(self, user, driver):
        email = user["email"]
        password = user["password"]

        main_page = MainPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_button_personal_account()
        personal_account_page.enter_email(email)
        personal_account_page.enter_password(password)
        main_page.finish_login_and_make_order()
        name = main_page.wait_and_find_confirmation()

        assert name.is_displayed()

    @allure.title('Проверка перехода по кнопке "Конструктор"')
    @allure.description('Кликаем на кнопку "Личный кабинет" и далее переходим по кнопке "Конструктор"')
    def test_click_button_constructor(self, driver):
        page = PersonalAccountPage(driver)
        page.click_button_personal_account()
        page.click_button_constructor()

        assert page.get_current_url() == Urls.BASE_PAGE

    @allure.title('Вход в раздел "История заказов')
    @allure.description('Регистрируем пользователя, логинимся, входим в личный кабинет, открываем "Историю заказов"')
    def test_click_history_profile(self, user, driver):
        email = user["email"]
        password = user["password"]

        page = PersonalAccountPage(driver)
        page.click_button_personal_account()
        page.enter_email(email)
        page.enter_password(password)
        page.click_enter_personal_account_wait_pages_changes()
        page.click_history_profile()

        assert page.get_current_url() == Urls.BASE_PAGE + Urls.HISTORY_ORDER_PAGE

    @allure.title('Выход из личного кабинета')
    @allure.description('Создаем, регистрируем пользователя, логинимся, входим в личный кабинет и выходим из него')
    def test_exit_account(self, user, driver):
        email = user["email"]
        password = user["password"]

        page = PersonalAccountPage(driver)
        page.click_button_personal_account()
        page.enter_email(email)
        page.enter_password(password)
        page.click_enter_personal_account_wait_pages_changes()
        page.click_exit_button()
        page.wait_for_url_changes_profile_account()

        assert page.get_current_url() == Urls.BASE_PAGE + Urls.LOGIN_PAGE

