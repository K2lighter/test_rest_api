from pydantic import BaseModel


class BookPydantic(BaseModel):
    """Класс для создания параметров валидации"""

    id: int
    name: str
    author: str
    year: int
    isElectronicBook: bool
