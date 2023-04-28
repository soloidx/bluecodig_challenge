from typing import Optional
from pydantic import BaseModel, HttpUrl


class BaseUri(BaseModel):
    origin: HttpUrl


class CreateUri(BaseUri):
    pass


class Uri(BaseUri):
    id: int
    count: int
    short_code: str
    title: Optional[str]

    class Config:
        orm_mode = True
