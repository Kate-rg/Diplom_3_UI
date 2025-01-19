from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure
from seletools.actions import drag_and_drop
from data import Urls
from pages.personal_account_page import PersonalAccountPage
from pages.main_page import MainPage


class OrderListPage(BasePage):
    @allure.step('Клик по кнопке "Ленте заказов')
    def click_order_feed(self):
        self.click(self.BUTTON_FEED)

    @allure.step('Находим заказ в ленте заказов с требуемым номером')
    def find_order_in_feed(self, number):
        order_locator = (By.XPATH, f"//div[contains(@class,'OrderFeed_contentBox__3-tWb')]//p[contains(text(), '{number}')]")
        element = self.find_element_with_wait(order_locator)
        return element

    @allure.step('Ищем заголовок карточки заказа')
    def wait_and_find_order_card(self):
        return self.find_element_with_wait(self.ORDER_CARD)

    @allure.step('Клик по карточке заказа')
    def click_order_card(self):
        self.click(self.ORDER_CARD)

    @allure.step('Ищем само всплывающее окно')
    def wait_and_find_order_card_window(self):
        return self.find_element_with_wait(self.ORDER_CARD_MODAL_WINDOW)

    @allure.step('Перетаскиваем ингредиент в корзину покупателя')
    def put_ingredient_into_basket(self):
        ingredient = self.find_element_with_wait(MainPage.INGREDIENT)
        basket = self.find_element_with_wait(MainPage.ORDER_BASKET)
        drag_and_drop(self.driver, ingredient, basket)

    @allure.step('Клик по кнопке "Личный кабинет"')
    def click_button_account(self):
        self.click(PersonalAccountPage.BUTTON_ACCOUNT)

    @allure.step('Клик по кнопке "Войти"')
    def click_enter_button(self):
        self.click(PersonalAccountPage.BUTTON_ENTER)

    @allure.step('Клик по кнопке "Оформить заказ"')
    def click_make_order(self):
        self.click(MainPage.BUTTON_MAKE_ORDER)

    @allure.step('Клик по крестику всплывающего окна')
    def click_cross(self):
        self.click(self.ORDER_CARD_MODAL_WINDOW_CROSS)

    @allure.step('Клик по кнопке "История заказов"')
    def click_history_profile(self):
        self.click(PersonalAccountPage.BUTTON_HISTORY_PROFILE)

    @allure.step('Входим в личный кабинет')
    def enter_account(self):
        self.click_button_account()
        self.wait_for_url_changes_main()
        self.wait_for_url_changes_profile()

    @allure.step('Входим в "Историю заказов", дожидаемся карточки заказа')
    def enter_profile_history(self):
        self.click_history_profile()
        self.wait_and_find_order_card()

    @allure.step('Входим под данными пользователя и оформляем заказ, кликнув по крестику окна')
    def place_order(self, email, password):
        personal_account_page = PersonalAccountPage(self.driver)
        personal_account_page.click_button_personal_account()
        personal_account_page.enter_email(email)
        personal_account_page.enter_password(password)

        self.click_enter_button()
        self.put_ingredient_into_basket()
        self.click_make_order()
        self.click_cross()

    @allure.step('Ищем текст по локатору "номер карточки заказа"')
    def get_order_number_text(self):
        return self.get_element_text(self.ORDER_NUMBER_CARD)

    @allure.step('Ищем текст по локатору левого блока с карточками заказов')
    def get_all_orders_text(self):
        return self.get_element_text(self.LEFT_BLOCK)

    @allure.step('Ожидание смены главной страницы')
    def wait_for_url_changes_main(self):
        self.wait_url_changes(Urls.BASE_PAGE)

    @allure.step('Ожидание смены страницы профайл')
    def wait_for_url_changes_profile(self):
        self.wait_url_changes(Urls.BASE_PAGE + Urls.ACCOUNT_PROFILE_PAGE)

    @allure.step('Поиск элемента левого блока с карточками заказов по локатору')
    def wait_and_find_left_block(self):
        return self.find_element_with_wait(self.LEFT_BLOCK)

    @allure.step('Кликнуть по кнопке "Лента заказов" и дождаться появления левого блока')
    def click_order_list_and_wait_left_block(self):
        self.click_order_feed()
        self.wait_and_find_left_block()

    @allure.step('Дождаться появления блока со счетчиком "За все время"')
    def wait_and_find_block_total(self):
        return self.find_element_with_wait(self.ORDER_COUNT_TOTAL)

    @allure.step('Получить текст из счетчика "За все время"')
    def block_total_number(self):
        return int(self.get_element_text(self.ORDER_COUNT_TOTAL))

    @allure.step('Дождаться появления блока со счетчиком "За сегодня')
    def wait_and_find_block_daily(self):
        return self.find_element_with_wait(self.ORDER_COUNT_DAY)

    @allure.step('Получить текст из счетчика "За сегодня"')
    def block_daily_number(self):
        return int(self.get_element_text(self.ORDER_COUNT_DAY))

    @allure.step('Кликнуть по кнопке "Лента заказов" и дождаться появления блока счетчика "За все время"')
    def click_order_list_and_find_block_total(self):
        self.click_order_feed()
        self.wait_and_find_block_total()

    @allure.step('Кликнуть по кнопке "Лента заказов" и дождаться появления блока счетчика "За сегодня"')
    def click_order_list_find_block_daily(self):
        self.click_order_feed()
        self.wait_and_find_block_daily()

    @allure.step('Дождаться появления блока раздела "В работе"')
    def wait_and_find_number_in_work(self):
        return self.find_element_with_wait(self.NUMBER_IN_WORK)

    @allure.step('Получить текст из блока раздела "В работе"')
    def number_in_work_text(self):
        return self.get_element_text(self.NUMBER_IN_WORK)

    @allure.step('Кликнуть по кнопке "Лента заказов" и дождаться появления блока раздела "В работе"')
    def click_order_list_find_in_work(self):
        self.click_order_feed()
        self.wait_and_find_number_in_work()

    BUTTON_FEED = (By.XPATH, "//p[text()='Лента Заказов']")
    ORDER_NUMBER_CARD = (By.XPATH, "(//p[@class='text text_type_digits-default'])[1]")
    ORDER_COUNT_TOTAL = (By.XPATH, "//div[@class='undefined mb-15']/p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")
    ORDER_COUNT_DAY = (By.XPATH, "(//div/p[@class='OrderFeed_number__2MbrQ text text_type_digits-large'])[2]")
    ORDER_CARD = (By.XPATH, "(//a[@class='OrderHistory_link__1iNby'])[1]")
    ORDER_CARD_MODAL_WINDOW_CROSS = (By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    ORDER_CARD_MODAL_WINDOW = (By.XPATH, "//div[@class='Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10']")
    LEFT_BLOCK = (By.XPATH, "//ul[@class='OrderFeed_list__OLh59']")
    NUMBER_IN_WORK = (By.XPATH, "(//li[contains(@class, 'text text_type_digits-default mb-2')])[6][1]")