from utils.baseclasses.response import Response
from utils.checking import Checking
from utils.api import Library_api
from utils.schemas.post import POST_SCHEMA
from jsonschema import validate
import allure

# Переменные для тестов

real_id = 1
fake_id = 212
zero_id = 0
json_for_create_new_book = {"name": "Война и мир"}
json_with_int_name = {"name": 21}
json_with_year = {"year": "ttt", "name": "Война и мир"}
json_with_author = {"author": "leo", "name": "Война и мир"}
json_with_is_electronic = {"isElectronicBook": "ttt", "name": "Война и мир"}


def test_get_all_books(set_up):
    """Получить список всех книг"""

    result_get = Library_api.get_all_books()
    check_post = result_get.json()
    validate(check_post, POST_SCHEMA)
    return Checking.check_status_code(result_get, 200)


def test_get_book_by_real_id(set_up):
    """Получить книгу по существующему id"""

    result_get = Library_api.get_new_book(str(real_id))
    return Checking.check_status_code(result_get, 200)


def test_get_book_by_fake_id(set_up):
    """Получить книгу по не существующему id"""

    result_get = Library_api.get_new_book(str(fake_id))
    return Checking.check_status_code(result_get, 404)


def test_get_book_by_zero_id(set_up):
    """Получить книгу по id равной нулю"""

    result_get = Library_api.get_new_book(str(zero_id))
    Checking.check_json_value_token(result_get, 'error', 'Book with id 0 not found')
    return Checking.check_status_code(result_get, 404)


def test_create_book_with_required_param(set_up):
    """Тестирование создание книги с 1 обязательным параметром name"""

    result_post = Library_api.create_book_with_required_param(json_for_create_new_book)
    name = result_post.json().get("book")["name"]  # получаем значение обязательного поля "name"
    book_id = result_post.json().get("book")["id"]
    Checking.check_status_code(result_post, 201)
    Checking.check_name_value(name, "Война и мир")
    return Library_api.delete_new_book(str(book_id))  # для удаления созданной книги


def test_param_year_in_json(set_up):
    """Проверка валидации поля - year, значение не должно быть строкой"""

    result_post = Library_api.create_book_with_required_param(json_with_year)  # негативный тест
    check_post = result_post.json()
    print(check_post)
    validate(check_post, POST_SCHEMA)
    return Checking.check_status_code(result_post, 400)


def test_param_name_in_json(set_up):
    """Проверка валидации поля - name, значение не должно быть числом"""

    result_post = Library_api.create_book_with_required_param(json_with_int_name)
    check_post = result_post.json()
    validate(check_post, POST_SCHEMA)
    Checking.check_json_value_token(result_post, 'error', 'Name must be String type (Unicode)')
    return Checking.check_status_code(result_post, 400)


def test_param_iselectronic_in_json(set_up):
    """Проверка валидации поля - isElectronic, значение не должно быть строкой"""

    result_post = Library_api.create_book_with_required_param(json_with_is_electronic)  # негативный тест
    check_post = Response(result_post)
    return check_post.assert_status_code(400).validate(POST_SCHEMA)


def test_update_param_name(set_up):
    """Порверка на возможность изменения значения поля name с сущ. значением"""

    result_post = Library_api.create_book_with_required_param(json_for_create_new_book)
    name = result_post.json().get("book")["name"]  # получаем значение обязательного поля "name"
    print(f"До изменения - {name}")
    book_id = result_post.json().get("book")["id"]
    result_put = Library_api.put_new_book(str(book_id))
    new_name = result_put.json().get("book")["name"]
    print(f"После изменения - {new_name}")
    Checking.check_name_value(new_name, "Евгений Онегин")
    Library_api.delete_new_book(str(book_id))  # для удаления созданной книги
    result_get = Library_api.get_new_book(str(book_id))
    return Checking.check_status_code(result_get, 404)

