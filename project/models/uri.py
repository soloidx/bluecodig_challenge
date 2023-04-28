from sqlalchemy import Column, Integer, String

from project.models.database import Base


class Uri(Base):
    __tablename__ = "uri"

    id = Column(Integer, primary_key=True, index=True)
    origin = Column(String, unique=True)
    short_code = Column(String, unique=True, index=True)
    count = Column(Integer, default=0)
    title = Column(String, default="")
