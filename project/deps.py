from contextlib import contextmanager

from typing import Generator

from project.models.database import SessionLocal


# this version is for FastAPI apis
def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# this version is for standalone scripts as a context
@contextmanager
def get_db_context() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
