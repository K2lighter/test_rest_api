from pydantic import BaseModel, Field


class POST(BaseModel):
    """Класс для создания параметров валидации"""

    book: str
    id: int
    name: str
    author: str
    year: int
    isElectronicBook: bool
