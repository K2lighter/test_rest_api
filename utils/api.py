from utils.http_methods import HttpMethods

base_url = 'http://192.168.1.64:5000/'


class Library_api:
    """Класс с методами, с помощью которых будем:
     добавлять, удалять, изменять, получать информацию"""

    @staticmethod
    def create_new_book():
        """Метод для создания новой книги"""
        json_for_create_new_book = {
            'name': 'Война и мир',
            'author': 'Лев Толстой',
            'year': 1869,
            'isElectronicBook': False
        }
        post_resource = '/api/books'
        post_url = base_url + post_resource
        print(post_url)
        result_post = HttpMethods.post(post_url, json_for_create_new_book)
        print(result_post.text)
        return result_post

    @staticmethod
    def get_new_book(book_id):
        """Метод для проверки создания новой книги"""
        get_resource = "/api/books/"
        get_url = base_url + get_resource + book_id
        print(get_url)
        result_get = HttpMethods.get(get_url)
        print(result_get.text)
        return result_get

    @staticmethod
    def put_new_book(book_id):
        """Метод для изменения новой книги"""
        put_resource = 'api/books/'
        put_url = base_url + put_resource + book_id
        print(put_url)
        json_for_update_new_book = {
            "id": book_id,
            "name": 'Евгений Онегин',
            "author": 'Александр Пушкин',
            "year": 1830,
            'isElectronicBook': False
        }
        result_put = HttpMethods.put(put_url, json_for_update_new_book)
        print(result_put.text)
        return result_put

    @staticmethod
    def delete_new_book(book_id):
        """Метод для удаления новой книги"""
        delete_resource = '/api/books/'
        delete_url = base_url + delete_resource + book_id
        json_for_delete_new_book = {
            "id": book_id
        }
        result_delete = HttpMethods.delete(delete_url, json_for_delete_new_book)
        print(result_delete.text)
        return result_delete

    @staticmethod
    def create_book_with_required_param(json):
        """Метод для создания книги с обязательным параметром name"""
        post_resource = '/api/books'
        post_url = base_url + post_resource
        print(post_url)
        result_post = HttpMethods.post(post_url, json)
        return result_post

    @staticmethod
    def get_all_books():
        get_resource = '/api/books'
        get_url = base_url + get_resource
        print(get_url)
        result_get = HttpMethods.get(get_url)
        return result_get
