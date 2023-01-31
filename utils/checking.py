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
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print(f"Успех, тест пройден!!! Поле {expected_value} присутствует")

    @staticmethod
    def check_value(keys_list, expected_value):
        """Метод для проверки наличия обязательных полей в ответах запроса"""

        if expected_value in keys_list:
            print(f"Успех, тест пройден!!! Обязательное поле {expected_value} присутствует")
        else:
            raise AssertionError(f"Провал, тест не пройден!!! Поле {expected_value} отсутствует")

    @staticmethod
    def check_name_value(actual_value, expected_value):
        """Метод для проверки значений обязательных полей в ответах запроса"""

        assert actual_value == expected_value, "Провал, тест не пройден!!! Факт. значение поля не равно ожидаемому"
        print("Успех, тест пройден!!! Фактическое значение поля равно ожидаемому")

    @staticmethod
    def check_json_value_token(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value, "Провал, тест не пройден!!! Факт. значение поля не равно ожидаемому"
        print(f'Успех, тест пройден!!! Фактическое значение поля {field_name} равно ожидаемому {expected_value}')

    @staticmethod
    def check_json_search_word_in_value(response: Response, field_name, search_word):
        check = response.json()
        check_info = check.get(field_name)
        if search_word in check_info:
            print(f"Успех, тест пройден!!! Слово {search_word} присутствует")
        else:
            raise AssertionError("Провал, тест не пройден!!! Слово отсутствует")



