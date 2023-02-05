import json

import pytest

import variables
from utils.api import Library_api


@pytest.fixture
def set_up():
    """
    Метод для обозначения начала и конца теста
    """
    print("START TEST")
    yield
    print("END TEST")


@pytest.fixture
def create_book():
    """
    Метод создает книгу все поля заполнены и валидны
    """
    Library_api.create_new_book(variables.json_all_valid_param_4)
    print("CREATE BOOK")


@pytest.fixture
def create_and_delete_book():
    """
    Метод создает новую книгу, все поля заполнены и валидны,
    затем выполняется внутренняя функция,
    в блоке yield новая книга удаляется
    """
    Library_api.create_new_book(variables.json_all_valid_param)
    print("CREATE BOOK")
    yield
    Library_api.delete_book_with_book_id(str(json.loads(Library_api.get_all_books().text)['books'][-1]['id']))
    print("DELETE BOOK")


@pytest.fixture
def delete_book():
    """Метод считает количество книг в базе до исполнения внутренней функции,
    затем исполняется внутренняя функция,
    в блоке yield посчитается снова количество книг в базе,
    если книга создалась, то она удаляется
    """

    count_book_before = len(json.loads(Library_api.get_all_books().text)['books'])
    yield
    last_book = str(json.loads(Library_api.get_all_books().text)['books'][-1]['id'])
    count_book_after = len(json.loads(Library_api.get_all_books().text)['books'])
    if count_book_after > count_book_before:
        Library_api.validate(
            Library_api.get_new_book(str(json.loads(Library_api.get_all_books().text)['books'][-1]['id'])).json()[
                "book"])
        Library_api.delete_book_with_book_id(last_book)
        print("DELETE BOOK")
