from utils.api import Library_api


class Test_create_book:
    """Создание, изменение и удаление новой книги"""

    def test_create_new_book(self):
        print('Method POST')
        result_post = Library_api.create_new_book()
        check_post = result_post.json()
        book_id = str(check_post.get("book")["id"])  # получаем id новой книги


