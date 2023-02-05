import allure
import pytest
from jsonschema import validate

import variables
from utils.api import Library_api
from utils.checking import Checking
from utils.schemas.post import POST_SCHEMA


@allure.epic("Check some functional")
class TestCases:
    """Класс с проверками функциональности"""

    @pytest.mark.development
    @allure.description("Get all book test")
    def test_get_all_books(self, set_up):
        """
        Получить список всех книг
        - Тесткейс id: 1
        """
        result_get = Library_api.get_all_books()
        check_post = result_get.json()
        print(check_post)
        validate(check_post, POST_SCHEMA)
        return Checking.check_status_code(result_get, 200)

    @pytest.mark.development
    @allure.description("Get book by id")
    def test_get_book_by_real_id(self, set_up):
        """
        Получить книгу по существующему id
        - Тесткейс id: 2
        """
        result_get = Library_api.get_new_book(str(variables.real_id))
        check_get = result_get.json()
        validate(check_get, POST_SCHEMA)
        return Checking.check_status_code(result_get, 200)

    @pytest.mark.development
    @allure.description("Get book by fake id")
    def test_get_book_by_fake_id(self, set_up):
        """
        Получить книгу по не существующему id
        - Тесткейс id: 4
        """
        result_get = Library_api.get_new_book(str(variables.fake_id))
        return Checking.check_status_code(result_get, 404)

    @pytest.mark.development
    @allure.description("Get book by id=0")
    def test_get_book_by_zero_id(self, set_up):
        """
        Получить книгу по id равной нулю
        - Тесткейс id: 5
        """
        result_get = Library_api.get_new_book(str(variables.zero_id))
        Checking.check_json_value_token(result_get, 'error', 'Book with id 0 not found')
        return Checking.check_status_code(result_get, 404)

    @pytest.mark.development
    @allure.description("Create book with 1 required param - 'name'")
    def test_create_book_with_required_param(self, set_up, delete_book):
        """
        Тестирование создание книги с 1 обязательным параметром 'name' на кириллице
        - Тесткейс id: 7
        """
        result_post = Library_api.create_new_book(variables.json_with_only_name)
        print("CREATE BOOK")
        name = result_post.json().get("book")["name"]  # получаем значение обязательного поля "name"
        Checking.check_name_value(name, "Война и мир")
        return Checking.check_status_code(result_post, 201)

    #
    @pytest.mark.development
    @allure.description("Check validation param - 'year'")
    def test_param_year(self, set_up):
        """
        Проверка валидации поля - year, значение не должно быть строкой
        - Тесткейс id: 14
        """
        result_post = Library_api.create_new_book(variables.json_with_str_year)  # негативный тест
        year = result_post.json().get("book")["year"]
        Checking.check_name_value(type(year), int)
        return Checking.check_status_code(result_post, 400)

    @pytest.mark.skip("this test realize with fixture in another file")
    @allure.description("Check validation param 'name'")
    def test_param_name(self, set_up):
        """
        Проверка валидации поля - name, значение не должно быть числом
        - Тесткейс id: 8
        """
        result_post = Library_api.create_new_book(variables.json_with_only_int_name)
        name = result_post.json().get("book")["name"]
        Checking.check_name_value(type(name), str)
        Checking.check_json_value_token(result_post, 'error', 'Name must be String type (Unicode)')
        return Checking.check_status_code(result_post, 400)

    #
    @pytest.mark.skip("this test realize with fixture in another file")
    @allure.description("Check update param 'name'")
    def test_update_param_name(self, set_up):
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
        Library_api.delete_new_book(str(book_id))  # для удаления созданной книги
        result_get = Library_api.get_new_book(str(book_id))
        return Checking.check_status_code(result_get, 404)

# python -m pytest --alluredir=allure_report/test_library_api.py
# allure serve allure_report/test_library_api.py
