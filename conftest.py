import pytest
import requests
from configuration import SERVICE_URL
from utils.api import Library_api
from tests.functional_test import book_id, json_for_create_new_book


@pytest.fixture()
def set_up():
    """Метод для обозначения начала и конца теста"""

    print("START TEST")

    yield

    print("END TEST")


@pytest.fixture()
def get_books():
    response = requests.get(SERVICE_URL)
    return response


@pytest.fixture
def create_and_delete_book():
    """CREATE AND DELETE BOOK"""

    Library_api.create_book_with_required_param(json_for_create_new_book)
    print("CREATE BOOK")

    yield

    Library_api.delete_new_book(book_id)
    print("DELETE BOOK")

