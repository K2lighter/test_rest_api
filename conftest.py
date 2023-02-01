import pytest


@pytest.fixture()
def set_up():
    print("START TEST")
    yield
    print(" END TEST")