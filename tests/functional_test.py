import json

import allure
import pytest

import variables
from utils.api import Library_api
from utils.checking import Checking

"""Функциональное тестирование с применением фикстур"""


@pytest.mark.development
@allure.description("Check name, after changed")
def test_method_put(set_up, create_and_delete_book):
    """
    Проверка на возможность изменения значения поля 'name' с сущ. значением на валидное для поля значение
    - Тесткейс id: 18
    """
    name_before_changed = json.loads(Library_api.get_all_books().text)['books'][-1]['name']
    print(f"Старое название: {name_before_changed}")
    test_object = Library_api.put_new_book(variables.json_all_valid_param_2)
    name_after_changed = json.loads(Library_api.get_all_books().text)['books'][-1]['name']
    print(f"Новое название: {name_after_changed}")
    Checking.check_name_value(name_after_changed, "Евгений Онегин")
    return Checking.check_status_code(test_object, 200)


@pytest.mark.development
@allure.description("Check create new book")
def test_method_create(set_up, delete_book):
    """
    Проверка на возможность создания новой книги, все поля заполнены и валидны
    - Тесткейс id: 13
    """

    print("CREATE BOOK")
    test_object = Library_api.create_new_book(variables.json_all_valid_param)
    name_book = test_object.json().get('book')['name']
    Checking.check_name_value(name_book, "Война и мир")
    print(f"Создана новая книга: {name_book}")
    return Checking.check_status_code(test_object, 201)


@pytest.mark.development
@allure.description("Check name validation")
def test_validation_name(set_up, delete_book):
    """
    Проверка валидации поля 'name' на невалидный для поля тип int
    - Тесткейс id: 8
    """
    test_object = Library_api.create_new_book(variables.json_with_only_int_name)
    Checking.check_json_value_token(test_object, 'error', 'Name must be String type (Unicode)')
    return Checking.check_status_code(test_object, 400)

# Library_api.validate(
# Library_api.get_new_book(str(json.loads(Library_api.get_all_books().text)['books'][-1]['id'])).json()["book"])
