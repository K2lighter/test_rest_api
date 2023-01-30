from utils.checking import Checking
from utils.api import Library_api


class Test_create_book:
    """ Тест на создание, изменение и удаление новой книги"""

    def test_create_new_book(self):
        print('Method POST - метод создание новой книги')
        result_post = Library_api.create_new_book()
        check_post = result_post.json()
        book_id = str(check_post.get("book")["id"])  # получаем id новой книги
        Checking.check_status_code(result_post, 201)

        print("Method GET after POST - для проверки создания новой книги")
        result_get = Library_api.get_new_book(book_id)
        check_get = list(result_get.json()["book"])  # получаем список ключей словаря "book"
        Checking.check_status_code(result_get, 200)
        Checking.check_value(check_get, 'name')

        print("Method PUT - метод для изменения новой книги")
        result_put = Library_api.put_new_book(book_id)
        Checking.check_status_code(result_get, 200)

        print("Method GET after PUT для проверки изменения инфы о новой книге")
        result_get = Library_api.get_new_book(book_id)
        Checking.check_status_code(result_get, 200)

        print("Method DELETE для удаления новой книги")
        result_delete = Library_api.delete_new_book(book_id)
        Checking.check_status_code(result_get, 200)

        print("Method GET after DELETE для проверки удаления новой книги")
        result_get = Library_api.delete_new_book(book_id)
        Checking.check_status_code(result_get, 404)
