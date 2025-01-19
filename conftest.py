import pytest
import allure
import helper
import requests
from selenium import webdriver
from data import Urls, ApiUrls


@allure.step('Запуск драйвера для каждого браузера - firefox и chrome')
@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    driver = None
    if request.param == 'chrome':
        driver = webdriver.Chrome()

    elif request.param == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Firefox(options=options)

    driver.get(Urls.BASE_PAGE)

    yield driver

    driver.quit()


@allure.step('Создание уникального пользователя и его регистрация с последующим удалением данных')
@pytest.fixture(scope='function')
def user():
    user = helper.TestMethodsHelper.create_random_login_password()
    response = requests.post(ApiUrls.BASE_URL_API + ApiUrls.REGISTER_USER_API, data=user)
    yield user

    token = response.json()["accessToken"]
    requests.delete(
        ApiUrls.BASE_URL_API + ApiUrls.DELETE_USER_API,
        data=user,
        headers={"Authorization": token})

