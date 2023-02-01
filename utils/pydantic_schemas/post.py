from pydantic import BaseModel, Field


class Post(BaseModel):
    """Класс для создания параметров валидации"""

    id: int
    name: str
    author: str
    year: int
    isElectronicBook: bool
