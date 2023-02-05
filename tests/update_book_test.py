import json

import allure
import pytest

import variables
from utils.api import Library_api
from utils.checking import Checking

"""Функциональное тестирование: метода update (put)"""


@pytest.mark.development
@allure.description("Check name, after changed")
def test_method_put_with_all_param(set_up, create_and_delete_book):
    """
    Проверка на возможность изменения значения поля 'name' с сущ. значением на валидное для поля значение
    - Тесткейс id: 18
    """
    name_before_changed = json.loads(Library_api.get_all_books().text)['books'][-1]['name']
    print(f"Старое название: {name_before_changed}")
    test_object = Library_api.put_new_book(variables.json_all_valid_param_4)
    name_after_changed = json.loads(Library_api.get_all_books().text)['books'][-1]['name']
    print(f"Новое название: {name_after_changed}")
    Checking.check_name_value(name_after_changed, "Евгений Онегин")
    return Checking.check_status_code(test_object, 200)


@pytest.mark.development
@allure.description("Check update book with valid param 'name' only")
def test_method_put(set_up, create_and_delete_book):
    """
    Проверка на возможность изменения книги только с 1 валидным параметром 'name'
    - Тесткейс id: 19
    """

    test_object = Library_api.put_new_book(variables.json_with_only_name)
    print(test_object.json())
    Checking.check_json_value_token(test_object, 'error', 'Author is required')
    return Checking.check_status_code(test_object, 400)


@pytest.mark.skip("this test realize with fixture in another test")
@allure.description("Check update param 'name'")
def test_update_param_name(set_up):
    """
    Проверка на возможность изменения значения поля name с сущ. значением
    - Тесткейс id: 18
    """
    result_post = Library_api.create_new_book(variables.json_all_valid_param)
    name = result_post.json().get("book")["name"]  # получаем значение обязательного поля "name"
    print(f"До изменения - {name}")
    book_id = result_post.json().get("book")["id"]
    result_put = Library_api.put_new_book(str(book_id))  # изменяем значение обязательного поля "name"
    new_name = result_put.json().get("book")["name"]
    print(f"После изменения - {new_name}")
    Checking.check_name_value(new_name, "Евгений Онегин")
    Library_api.delete_book_with_book_id(str(book_id))  # для удаления созданной книги
    result_get = Library_api.get_new_book(str(book_id))
    return Checking.check_status_code(result_get, 404)

