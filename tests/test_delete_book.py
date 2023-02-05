import json

import allure
import pytest

import variables
from utils.api import Library_api
from utils.checking import Checking


@pytest.mark.development
@allure.description("Check create book without param 'name'")
def delete_book_with_all_valid_param(set_up):
    """
    Проверка на возможность удаления книги, все поля заполнены и валидны
    - Тесткейс id: 28
    """
    Library_api.create_new_book(variables.json_all_valid_param_4)
    last_book = str(json.loads(Library_api.get_all_books().text)['books'][-1]['id'])
    result_delete = Library_api.delete_new_book(last_book)
    Checking.check_status_code(result_delete, 200)
    Checking.check_json_value_token(result_delete, 'result', True)