import requests
from configuration import SERVICE_URL


def test_getting_book_list():

    response = requests.get(SERVICE_URL)
    print(response)
    test_object = response.json()
    print(test_object)

