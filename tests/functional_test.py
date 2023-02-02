from utils.baseclasses.response import Response
from utils.enums.global_enums import GlobalErrorMessages
from utils.checking import Checking
from utils.api import Library_api
from utils.schemas.post import POST_SCHEMA
from jsonschema import validate
import allure

# Переменные для тестов

real_id = 1
zero_id = 0
fake_id = 99999999999
json_for_create_new_book = {"name": "Война и мир"}
json_with_int_name = {"name": 21}
json_with_year = {"year": "ttt", "name": "Война и мир"}
json_with_author = {"author": "leo", "name": "Война и мир"}
json_with_str_isElectronic = {"isElectronicBook": "ttt", "name": "Война и мир"}
result_post = Library_api.create_book_with_required_param(json_for_create_new_book)
name = result_post.json().get("book")["name"]  # получаем значение обязательного поля "name"
book_id = str(result_post.json().get("book")["id"])  # получаем значение обязательного поля "name"
result_put = Library_api.put_new_book(book_id)  # изменяем значение обязательного поля "name"
new_name = result_put.json().get("book")["name"]  # получаем новое значение обязательного поля "name"

"""Функциональное тестирование с применением фикстур"""


def test_method_put(set_up, create_and_delete_book):
    """Порверка на возможность изменения значения поля name с сущ. значением"""

    Checking.check_name_value(name, "Война и мир")
    print(f"Старое название: {name}")
    test_object = Library_api.put_new_book(book_id)
    Checking.check_status_code(test_object, 200)
    print(f"Новое название: {new_name}")
    Checking.check_name_value(new_name, "Евгений Онегин")


