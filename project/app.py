from typing import List

from fastapi import FastAPI, Depends, status, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from project import crud
from project.deps import get_db
from project.schemas import CreateUri, Uri
from settings import settings

app = FastAPI(title=settings.PROJECT_NAME)


@app.get("/healthcheck/")
def read_root():
    return {"status": "ok"}


@app.get("/{short_code}")
def redirect_url(short_code: str, db: Session = Depends(get_db)):
    origin_url = crud.visit_uri(db, short_code=short_code)
    if origin_url is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return RedirectResponse(url=origin_url, status_code=status.HTTP_302_FOUND)


def remove_query_params(uri: str):
    return uri.split("?")[0]


@app.post("/uri/", response_model=Uri, status_code=status.HTTP_201_CREATED)
def create_short_uri(original_uri: CreateUri, db: Session = Depends(get_db)):
    original_uri.origin = remove_query_params(original_uri.origin)
    uri_obj = crud.create_short_url(db, create_uri=original_uri)
    return uri_obj


@app.get("/uri/", response_model=List[Uri])
def get_top_uris(db: Session = Depends(get_db)):
    return crud.get_top_uri(db)
