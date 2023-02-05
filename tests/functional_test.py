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




# Library_api.validate(
# Library_api.get_new_book(str(json.loads(Library_api.get_all_books().text)['books'][-1]['id'])).json()["book"])
