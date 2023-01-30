import json
from requests import Response


class Checking:
    """Класс с методами для получения ответа от наших запросов"""

    @staticmethod
    def check_status_code(response: Response, status_code):
        """Метод для проверки статуса кода"""
        assert status_code == response.status_code
        if status_code == response.status_code:
            print(f"Успех, тест пройден!!! Статус код = {response.status_code}")
        else:
            print(f"Провал, тест не пройден!!! Статус код = {response.status_code}")

    @staticmethod
    def check_value(keys_list, expected_value):
        """Метод для проверки наличия обязательных полей в ответах запроса"""

        if expected_value in keys_list:
            print(f"Успех, тест пройден!!! Обязательное поле {expected_value} присутствует")
        else:
            raise AssertionError(f"Провал, тест не пройден!!! Поле {expected_value} отсутствует")
