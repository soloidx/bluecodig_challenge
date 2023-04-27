from typing import List
from pydantic import BaseModel, HttpUrl


class BaseUri(BaseModel):
    origin: HttpUrl


class CreateUri(BaseUri):
    pass


class Uri(BaseUri):
    id: int
    count: int
    short_code: str

    class Config:
        orm_mode = True
