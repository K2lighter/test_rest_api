from flask import Flask, jsonify, request
import emoji

app = Flask(__name__)

books = [
    {
        'id': 1,
        'name': u'Чистый код',
        'author': u'Роберт Мартин',
        'year': 1998,
        'isElectronicBook': False
    },
    {
        'id': 2,
        'name': u'Алгоритмы: построение и анализ',
        'author': u'Томас Кормен, Чарльз Лейзерсон',
        'year': 1989,
        'isElectronicBook': True
    }]


@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify({'books': books})


@app.route('/api/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = [book for book in books if book['id'] == book_id]
    if not book:
        return jsonify({'error': f'Book with id {book_id} not found'}), 404
    return jsonify({'book': book[0]})


@app.route('/api/books', methods=['POST'])
def create_book():
    if not request.json or not 'name' in request.json:
        return jsonify({'error': f'Name is required'}), 400
    name = request.json['name']
    if not isinstance(name, str) or is_string_contains_emoji(name):
        return jsonify({'error': f'Name must be String type (Unicode)'}), 400
    book = {

        'id': books[-1]['id'] + 1,
        'name': request.json['name'],
        'author': request.json.get('author', ""),
        'year': request.json.get('year', 0),
        'isElectronicBook': request.json.get('isElectronicBook', False)
    }
    books.append(book)
    return jsonify({'book': book}), 201


@app.route('/api/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = [book for book in books if book['id'] == book_id]
    if not book:
        return jsonify({'error': f'Book with id {book_id} not found'}), 404
    if not request.json:
        return jsonify({'error': f'Not found request Json body'}), 400

    if not 'name' in request.json:
        return jsonify({'error': f'Name is required'}), 400
    name = request.json['name']
    if not isinstance(name, str) or is_string_contains_emoji(name):
        return jsonify({'error': f'Name must be String type (Unicode)'}), 400

    if not 'author' in request.json:
        return jsonify({'error': f'Author is required'}), 400
    author = request.json['author']
    if not isinstance(author, str) or is_string_contains_emoji(author):
        return jsonify({'error': f'Author must be String type (Unicode)'}), 400

    if not 'year' in request.json:
        return jsonify({'error': f'Year is required'}), 400
    year = request.json['year']
    if not isinstance(year, int):
        return jsonify({'error': f'Year must be Int type'}), 400

    if not 'isElectronicBook' in request.json:
        return jsonify({'error': f'IsElectronicBook is required'}), 400
    isElectronicBook = request.json['isElectronicBook']
    if not isinstance(isElectronicBook, bool):
        return jsonify({'error': f'IsElectronicBook must be Bool type'}), 400

    book[0]['name'] = request.json.get('name', book[0]['name'])
    book[0]['author'] = request.json.get('author', book[0]['author'])
    book[0]['year'] = request.json.get('year', book[0]['year'])
    book[0]['isElectronicBook'] = request.json.get('isElectronicBook', book[0]['isElectronicBook'])
    return jsonify({'book': book[0]})


@app.route('/api/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = [book for book in books if book['id'] == book_id]
    if not book:
        return jsonify({'error': f'Book with id {book_id} not found'}), 404
    books.remove(book[0])
    return jsonify({'result': True})


def is_string_contains_emoji(str):
    for char in str:
        if emoji.is_emoji(char):
            return True
    return False


if __name__ == '__main__':
    app.run(host='0.0.0.0')
