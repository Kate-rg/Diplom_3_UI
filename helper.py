import random
import string
import allure

class TestMethodsHelper:
    @staticmethod
    @allure.step('Создание рандомных регистрационных данных')
    def create_random_login_password():
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        login = f'{generate_random_string(10)}@ya.ru'
        password = generate_random_string(10)
        name = generate_random_string(10)

        return {"email": login, "password": password, "name": name}

