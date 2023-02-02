from enum import Enum


class GlobalErrorMessages(Enum):
    """Класс для создания сообщений ошибок"""

    WRONG_STATUS_CODE = "Received status code is not equal to expected."
    WRONG_ELEMENT = "Element not found"
    WRONG_COMPARISON = "Actual result not equal expected"
