from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure
from seletools.actions import drag_and_drop
from pages.personal_account_page import PersonalAccountPage


class MainPage(BasePage):
    @allure.step('Клик по кнопке "Конструктор"')
    def click_button_constructor(self):
        self.click(self.BUTTON_CONSTRUCTOR)

    @allure.step('Клик по ингредиенту"')
    def click_ingredient(self):
        self.click(self.INGREDIENT)

    @allure.step('Ищем заголовок всплывающего окна')
    def wait_and_find_header(self):
        return self.find_element_with_wait(self.POPUP_WINDOW_HEADER)

    @allure.step('Закрываем по крестику всплывающее окно')
    def click_close_window(self):
        self.click(self.CLOSE_BUTTON)

    @allure.step('Находим невидимый крестик для закрытия окна')
    def cross_is_displayed(self):
        cross = self.wait_and_find_element_invisible(self.CLOSE_BUTTON)
        return cross.is_displayed()

    @allure.step('Перетаскиваем ингредиент в корзину покупателя')
    def put_ingredient_into_basket(self):
        ingredient = self.find_element_with_wait(self.INGREDIENT)
        basket = self.find_element_with_wait(self.ORDER_BASKET)
        drag_and_drop(self.driver, ingredient, basket)

    @allure.step('Ищем текст по локатору ингредиента')
    def get_ingredient_text(self):
        return self.get_element_text(self.INGREDIENT)

    @allure.step('Клик по кнопке "Оформить заказ"')
    def click_make_order(self):
        self.click(self.BUTTON_MAKE_ORDER)

    @allure.step('Ищем текст о подтверждении заказа')
    def wait_and_find_confirmation(self):
        return self.find_element_with_wait(self.CONFIRMATION_TEXT)

    @allure.step('Клик по кнопке "Войти"')
    def click_enter_button(self):
        self.click(PersonalAccountPage.BUTTON_ENTER)

    @allure.step('Завершить логин пользователя и оформит заказ')
    def finish_login_and_make_order(self):
        self.click_enter_button()
        self.put_ingredient_into_basket()
        self.click_make_order()


    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")
    INGREDIENT = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6c']/div/p[@class='counter_counter__num__3nue1']")
    POPUP_WINDOW_HEADER = (By.XPATH, "//h2[text()='Детали ингредиента']")
    CLOSE_BUTTON = (By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    ORDER_BASKET = (By.XPATH, "//ul[@class='BurgerConstructor_basket__list__l9dp_']")
    BUTTON_MAKE_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")
    CONFIRMATION_TEXT = (By.XPATH, "//p[text()='Ваш заказ начали готовить']")