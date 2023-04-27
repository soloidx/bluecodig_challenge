from fastapi import FastAPI, Depends, status

from sqlalchemy.orm import Session
from settings import settings
from project.schemas import CreateUri, Uri
from project import crud
from project.deps import get_db

app = FastAPI(title=settings.PROJECT_NAME)


@app.get("/healthcheck")
def read_root():
    return {"status": "ok"}


@app.get("/")
def read_root():
    return {"foo": "bar"}


@app.post("/uri", response_model=Uri, status_code=status.HTTP_201_CREATED)
def create_short_uri(original_uri: CreateUri, db: Session = Depends(get_db)):
    uri_obj = crud.create_short_url(db, create_uri=original_uri)
    return uri_obj
