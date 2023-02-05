import json

import allure
import pytest

import variables
from utils.api import Library_api
from utils.checking import Checking


@pytest.mark.development
@allure.description("Check create book without param 'name'")
def test_create_without_name(set_up, delete_book):
    """
    Проверка на возможность создания книги без обязательного поля 'name', остальные поля заполнены и валидны
    - Тесткейс id: 10
    """
    test_object = Library_api.create_new_book(variables.json_without_required_param_name)
    Checking.check_json_value_token(test_object, 'error', 'Name is required')
    return Checking.check_status_code(test_object, 400)


@pytest.mark.development
@allure.description("Check create book without params")
def test_create_without_params(set_up, delete_book):
    """
    Проверка на возможность создания книги без параметров (пустым телом запроса)
    - Тесткейс id: 27
    """
    test_object = Library_api.create_new_book(variables.json_without_params)
    Checking.check_json_value_token(test_object, 'error', 'Name is required')
    return Checking.check_status_code(test_object, 400)


@pytest.mark.development
@allure.description("Check create book with 2 valid params('name' and 'author')")
def test_create_with_two_valid_params(set_up, delete_book):
    """
    Проверка на возможность создания книги только с двумя валидными значениями('name', 'author')
    - Тесткейс id: 11
    """
    test_object = Library_api.create_new_book(variables.json_with_str_author)
    return Checking.check_status_code(test_object, 201)


@pytest.mark.development
@allure.description("Check create book with 3 valid params('name', 'author' and 'isElectronicBook')")
def test_create_without_params(set_up, delete_book):
    """
    Проверка на возможность создания книги с тремя валидными параметрами('name', 'author' and 'isElectronicBook')
    - Тесткейс id: 12
    """
    test_object = Library_api.create_new_book(variables.json_all_valid_param_3)
    return Checking.check_status_code(test_object, 201)


@pytest.mark.development
@allure.description("Check create new book")
def test_method_create(set_up, delete_book):
    """
    Проверка на возможность создания новой книги, все поля заполнены и валидны
    - Тесткейс id: 13
    """

    test_object = Library_api.create_new_book(variables.json_all_valid_param)
    return Checking.check_status_code(test_object, 201)


@pytest.mark.development
@allure.description("Check type int name validation")
def test_validation_name(set_up, delete_book):
    """
    Проверка на возможность создания новой книги c значением 'name' c тип int
    - Тесткейс id: 8
    """
    test_object = Library_api.create_new_book(variables.json_with_only_int_name)
    Checking.check_json_value_token(test_object, 'error', 'Name must be String type (Unicode)')
    return Checking.check_status_code(test_object, 400)


@pytest.mark.development
@allure.description("Check create new book with type 'year' = str")
def test_method_create(set_up, delete_book):
    """
    Проверка на возможность создания новой книги, с типом 'year' = str, остальные поля заполнены и валидны
    - Тесткейс id: 14
    """

    test_object = Library_api.create_new_book(variables.json_with_str_year)
    return Checking.check_status_code(test_object, 400)


@pytest.mark.development
@allure.description("Check validation param 'isElectronic'")
def test_validation_electronic(set_up, delete_book):
    """
    Проверка на возможность создания новой книги, с типом 'isElectronic' = str, остальные поля заполнены и валидны
    - Тесткейс id: 15
    """
    test_object = Library_api.create_new_book(variables.json_with_str_isElectronic)  # негативный тест
    return Checking.check_status_code(test_object, 400)
