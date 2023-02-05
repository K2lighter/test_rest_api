import allure
import pytest

import variables
from utils.api import Library_api
from utils.checking import Checking


@pytest.mark.development
@allure.description("Check delete book with real id")
def test_delete_book_with_real_id(set_up, create_book):
    """
    Проверка на возможность удаления книги по существующему id
    - Тесткейс id: 28
    """

    result_delete = Library_api.delete_new_book()
    print(result_delete.json())
    Checking.check_json_value_token(result_delete, 'result', True)
    return Checking.check_status_code(result_delete, 200)


@pytest.mark.development
@allure.description("Check delete book with fake id")
def test_delete_book_with_fake_id(set_up):
    """
    Проверка на возможность удаления книги по не существующему id
    - Тесткейс id: 29
    """
    result_delete = Library_api.delete_book_with_book_id(str(variables.fake_id))
    print(result_delete.json())
    Checking.check_status_code(result_delete, 404)


@pytest.mark.development
@allure.description("Check create book with id = 0")
def test_delete_book_with_zero_id(set_up):
    """
    Проверка на возможность удаления книги по id = 0
    - Тесткейс id: 30
    """
    result_delete = Library_api.delete_book_with_book_id(str(variables.zero_id))
    print(result_delete.json())
    Checking.check_status_code(result_delete, 404)


