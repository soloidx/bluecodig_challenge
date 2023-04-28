import base64
from typing import Optional, List
from sqlalchemy.orm import Session
from sqlalchemy import or_

from project.schemas import CreateUri, Uri
from project.models import uri as uri_model
from project.scrapper import get_title


def generate_short_code(code: str) -> str:
    return base64.urlsafe_b64encode(code.encode()).decode()


def create_short_url(db: Session, create_uri: CreateUri) -> Uri:
    db_obj: Optional[uri_model.Uri] = (
        db.query(uri_model.Uri).filter(uri_model.Uri.origin == create_uri.origin).first()
    )

    if db_obj is None:
        db_obj = uri_model.Uri(**create_uri.dict())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)

    db_obj.short_code = generate_short_code(str(db_obj.id))
    db.commit()
    return db_obj


def visit_uri(db: Session, short_code: str) -> str:
    db_obj: Optional[uri_model.Uri] = (
        db.query(uri_model.Uri).filter(uri_model.Uri.short_code == short_code).first()
    )

    if db_obj is None:
        return None

    db_obj.count += 1
    db.add(db_obj)
    db.commit()
    return db_obj.origin


def get_top_uri(db: Session) -> List[uri_model.Uri]:
    return db.query(uri_model.Uri).order_by(uri_model.Uri.count.desc()).limit(100).all()


def analyze_pages(db: Session):
    pages = db.query(uri_model.Uri).filter(or_(uri_model.Uri.title == "", uri_model.Uri.title.is_(None)))
    for page in pages:
        page.title = get_title(page.origin)
    db.commit()
