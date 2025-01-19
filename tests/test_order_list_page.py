import allure

from data import Urls
from pages.order_list_page import OrderListPage


class TestOrderList:
    @allure.title('Проверка перехода по кнопке "Лента заказов"')
    @allure.description('Кликаем на кнопку "Лента заказов" и переходим на страницу с заказами')
    def test_click_button_order_list(self, driver):
        page = OrderListPage(driver)
        page.click_order_feed()

        assert page.get_current_url() == Urls.BASE_PAGE + Urls.ORDER_LIST_PAGE

    @allure.title('Проверка открытия окна с заказом')
    @allure.description('Кликаем на "Ленту заказов", далее на любую карточку заказа, ждем открытия окна с заказом')
    def test_click_order_card(self, driver):
        page = OrderListPage(driver)
        page.click_order_feed()
        page.wait_and_find_order_card()
        page.click_order_card()
        order = page.wait_and_find_order_card_window()

        assert order.is_displayed()

    @allure.title('Проверка отображения сделанного заказа в ленте заказов')
    @allure.description('Логинимся на сайте, оформляем заказ, смотрим номер заказа, идем в ленту заказа и проверяем что заказ есть')
    def test_make_order_and_check_order_list(self, user, driver):
        email = user["email"]
        password = user["password"]
        page = OrderListPage(driver)

        page.place_order(email, password)
        page.enter_account()
        page.enter_profile_history()
        order_number = page.get_order_number_text()
        page.click_order_list_and_wait_left_block()
        orders_list = page.get_all_orders_text()

        assert order_number in orders_list

    @allure.title('Проверка увеличения счетчика "За все время" после оформления нового заказа')
    @allure.description('Логинюсь, оформляю заказ и проверяю, что счетчик "За все время" увеличился')
    def test_counter_total_changes(self, user, driver):
        email = user["email"]
        password = user["password"]
        page = OrderListPage(driver)

        page.click_order_list_and_find_block_total()
        counter_old = page.block_total_number()

        page.place_order(email, password)
        page.click_order_list_and_find_block_total()

        counter_new = page.block_total_number()

        assert counter_new > counter_old

    @allure.title('Проверка увеличения счетчика "За сегодня" после оформления нового заказа')
    @allure.description('Логинюсь, оформляю заказ и проверяю, что счетчик "За сегодня" увеличился')
    def test_counter_daily_changes(self, user, driver):
        email = user["email"]
        password = user["password"]
        page = OrderListPage(driver)

        page.click_order_list_find_block_daily()

        counter_old = page.block_daily_number()

        page.place_order(email, password)
        page.click_order_list_find_block_daily()

        counter_new = page.block_daily_number()

        assert counter_new > counter_old

    @allure.title('Проверка отображения созданного заказа в разделе "лента заказов"')
    @allure.description('Логинюсь, оформляю заказ и проверяю, что заказ отобразился в разделе "лента заказов"')
    def test_make_order_and_check_order_in_work(self, user, driver):
        email = user["email"]
        password = user["password"]
        page = OrderListPage(driver)

        page.place_order(email, password)

        page.enter_account()
        page.enter_profile_history()

        order_number_from_profile = page.get_order_number_text()
        page.click_order_feed()
        order = page.find_order_in_feed(order_number_from_profile)

        assert order is not None

