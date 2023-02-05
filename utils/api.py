import json

from pydantic import ValidationError

from utils.http_methods import HttpMethods
from utils.pydantic_schemas.post import BookPydantic

base_url = 'http://192.168.1.64:5000/'


class Library_api:
    """Класс с методами, с помощью которых будем:
     добавлять, удалять, изменять, получать информацию"""

    @staticmethod
    def create_new_book(json_post):
        """Метод для создания новой книги"""
        post_resource = '/api/books'
        post_url = base_url + post_resource
        print(post_url)
        result_post = HttpMethods.post(post_url, json_post)
        return result_post

    @staticmethod
    def get_new_book(book_id):
        """Метод для проверки создания новой книги"""
        get_resource = "/api/books/"
        get_url = base_url + get_resource + book_id
        print(get_url)
        result_get = HttpMethods.get(get_url)
        return result_get

    @staticmethod
    def put_new_book(json_put):
        """Метод для изменения новой книги"""
        put_resource = 'api/books/'
        book_id = str(json.loads(Library_api.get_all_books().text)['books'][-1]['id'])
        put_url = base_url + put_resource + book_id
        print(put_url)
        result_put = HttpMethods.put(put_url, json_put)
        return result_put

    @staticmethod
    def delete_new_book():
        """Метод для удаления новой книги"""
        delete_resource = '/api/books/'
        book_id = str(json.loads(Library_api.get_all_books().text)['books'][-1]['id'])
        delete_url = base_url + delete_resource + book_id
        result_delete = HttpMethods.delete(delete_url)
        return result_delete

    @staticmethod
    def delete_book_with_book_id(book_id):
        """Метод для удаления новой книги"""
        delete_resource = '/api/books/'
        delete_url = base_url + delete_resource + book_id
        result_delete = HttpMethods.delete(delete_url)
        return result_delete

    @staticmethod
    def get_all_books():
        """Метод для получения всех книг"""
        get_resource = '/api/books'
        get_url = base_url + get_resource
        result_get = HttpMethods.get(get_url)
        return result_get

    @staticmethod
    def validate(json_validate):
        """
        Метод для валидации всех полей согласно схеме pydantic
        """
        try:
            post = BookPydantic.parse_obj(json_validate)
        except ValidationError as error:
            print("Exception", error.json())
        else:
            print(f"тип name = {type(post.name)}, тип year =  {type(post.year)}"
                  f"\nтип author = {type(post.author)}, тип isElectronicBook = {type(post.isElectronicBook)}")
