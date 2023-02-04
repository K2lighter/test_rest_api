import json
import variables
import pytest

from utils.api import Library_api


@pytest.fixture()
def set_up():
    """Метод для обозначения начала и конца теста"""
    print("START TEST")
    yield
    print("END TEST")


@pytest.fixture
def create_and_delete_book():
    """CREATE AND DELETE BOOK"""
    Library_api.create_new_book(variables.json_all_valid_param)
    print("CREATE BOOK")
    yield
    Library_api.delete_new_book(str(json.loads(Library_api.get_all_books().text)['books'][-1]['id']))
    print("DELETE BOOK")


@pytest.fixture
def delete_book():
    """DELETE BOOK"""

    count_book_before = len(json.loads(Library_api.get_all_books().text)['books'])
    yield
    last_book = str(json.loads(Library_api.get_all_books().text)['books'][-1]['id'])
    count_book_after = len(json.loads(Library_api.get_all_books().text)['books'])
    if count_book_after > count_book_before:
        Library_api.delete_new_book(last_book)
        print("DELETE BOOK")
