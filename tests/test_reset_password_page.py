import allure
from pages.reset_password_page import ResetPasswordPage
from data import Urls


class TestResetPasswordPage:

    @allure.title('Проверка перехода на страницу восстановления пароля')
    @allure.description('Проверяем, что по кнопке "Восстановить пароль" мы попадаем на страницу восстановления пароля')
    def test_get_reset_password_page(self, driver):
        page = ResetPasswordPage(driver)
        page.enter_and_click_reset_password()
        assert page.get_current_url() == Urls.BASE_PAGE + Urls.FORGOT_PASSWORD_PAGE

    @allure.title('Проверка ввода почты ик лика по кнопка "Восстановить"')
    @allure.description('Проверяем, что можно заполнить поле почты и отправить данные по кнопке "Восстановить"')
    def test_input_email_and_reset(self, driver):
        page = ResetPasswordPage(driver)
        page.enter_and_click_reset_password()
        page.set_email_and_click_restore_button()
        page.wait_for_url_changes_restore()
        assert page.get_current_url() == Urls.BASE_PAGE + Urls.RESET_PASSWORD_PAGE

    @allure.title('Проверка активации поля для восстановления пароля через клик по "глазу"')
    @allure.description('Проверяем, что кликнув на "глаз" в поле ввода пароля, само поле становится активным')
    def test_active_password_field(self, driver):
        page = ResetPasswordPage(driver)
        page.enter_and_click_reset_password()
        page.set_email_and_click_restore_button()
        page.wait_for_url_changes_restore()
        before_click_eye = page.get_input_password_status()
        page.click_eye()
        after_click_eye = page.get_input_password_status()

        assert (before_click_eye is False and after_click_eye is True)
