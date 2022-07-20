from sqlalchemy.orm import Session

from sql import models
from sql import schemas


def get_city(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.City).offset(skip).limit(limit).all()


def create_city(db: Session, item: schemas.CityCreate):
    db_city = models.City(**item.dict())
    db.add(db_city)
    db.commit()
    db.refresh(db_city)
    return db_city


def update_city(db: Session, id: schemas.City, title: schemas.CityBase):
    db_city = get_city(db=db)
    db_city.id = id
    db_city.name = title
    db.commit()
    db.refresh(db_city)
    return db_city


def delete_city(db: Session):
    db_city = get_city(db=db)
    db.delete(db_city)
    db.commit()
