import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Кликаем по элементу с нужным локатором')
    def click(self, locator):
        button = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", button)

    @allure.step('Получить текущий адрес страницы')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Ожидание появления элемента по локатору')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Ожидание загрузки страницы')
    def wait_url_changes(self, url):
        WebDriverWait(self.driver, 3).until(expected_conditions.url_changes(url))

    @allure.step('Ожидание, пока нужный элемент по локатору не исчезнет')
    def wait_and_find_element_invisible(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Дожидаемся появления элемента и возвращаем его текст')
    def get_element_text(self, locator):
        return self.find_element_with_wait(locator).text
