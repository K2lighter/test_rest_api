import json
import allure
import pytest
from utils.api import Library_api
from utils.checking import Checking

# Переменные для тестов

real_id = 1
zero_id = 0
fake_id = 99999999999
json_for_create_new_book = {"name": "Война и мир"}
json_with_int_name = {"name": 21}
json_with_year = {"year": "ttt", "name": "Война и мир"}
json_with_author = {"author": "leo", "name": "Война и мир"}
json_with_str_isElectronic = {"isElectronicBook": "ttt", "name": "Война и мир"}

"""Функциональное тестирование с применением фикстур"""


@pytest.mark.development
@allure.description("Check name, after changed")
def test_method_put(set_up, create_and_delete_book):
    """
    Проверка на возможность изменения значения поля 'name' с сущ. значением на валидное для поля значение
    - Тесткейс id: 18
    """

    print(f"Старое название: {json.loads(Library_api.get_all_books().text)['books'][-1]['name']}")
    test_object = Library_api.put_new_book(str(json.loads(Library_api.get_all_books().text)['books'][-1]['id']))
    print(f"Новое название: {json.loads(Library_api.get_all_books().text)['books'][-1]['name']}")
    Checking.check_name_value(json.loads(Library_api.get_all_books().text)['books'][-1]['name'], "Евгений Онегин")
    return Checking.check_status_code(test_object, 200)


@pytest.mark.development
@allure.description("Check create new book")
def test_method_create(set_up, delete_book):
    """
    Проверка на возможность создания новой книги, все поля заполнены и валидны
    - Тесткейс id: 13
    """

    print("CREATE BOOK")
    test_object = Library_api.create_new_book()
    Checking.check_name_value(test_object.json().get('book')['name'], "Война и мир")
    print(f"Создана новая книга: {test_object.json().get('book')['name']}")
    return Checking.check_status_code(test_object, 201)


@pytest.mark.development
@allure.description("Check name validation")
def test_validation_name(set_up):
    """
    Проверка валидации поля 'name' на невалидный для поля тип int
    - Тесткейс id: 8
    """

    test_object = Library_api.create_book_with_required_param(json_with_int_name)
    Checking.check_json_value_token(test_object, 'error', 'Name must be String type (Unicode)')
    return Checking.check_status_code(test_object, 400)


@pytest.mark.development
@allure.description("Check name validation")
def test_validation_name(set_up):
    """
    Проверка валидации поля 'name' на невалидный для поля тип int
    - Тесткейс id: 8
    """

    test_object = Library_api.create_book_with_required_param(json_with_int_name)
    Library_api.validate(
        Library_api.get_new_book(str(json.loads(Library_api.get_all_books().text)['books'][-1]['id'])).json()["book"])
    Checking.check_json_value_token(test_object, 'error', 'Name must be String type (Unicode)')
    return Checking.check_status_code(test_object, 400)
