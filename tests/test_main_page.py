import allure

from pages.main_page import MainPage


class TestMainPage:
    @allure.title('Проверка появления всплывающего окна при клике на ингредиент')
    @allure.description('Кликаем на любой ингредиент и получаем всплывающее окно')
    def test_popup_window(self, driver):
        page = MainPage(driver)
        page.click_ingredient()
        popup_header = page.wait_and_find_header()

        assert popup_header.is_displayed()

    @allure.title('Проверка закрытия модального окна')
    @allure.description('Кликаем на крестик чтобы закрыть модальное окно')
    def test_close_popup_window(self, driver):
        page = MainPage(driver)
        page.click_ingredient()
        page.click_close_window()

        assert not page.cross_is_displayed()

    @allure.title('Проверка изменения счетчика заказа')
    @allure.description('Перетаскиваем ингредиент в корзину и проверяем изменения счетчика заказа')
    def test_put_ingredient_into_basket(self, driver):
        page = MainPage(driver)
        page.put_ingredient_into_basket()
        result_new = page.get_ingredient_text()

        assert result_new == '2'
