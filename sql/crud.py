from sqlalchemy.orm import Session

from sql import models
from sql import schemas


def getCity(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.City).offset(skip).limit(limit).all()


def createCity(db: Session, item: schemas.CityCreate):
    db_city = models.City(**item.dict())
    db.add(db_city)
    db.commit()
    db.refresh(db_city)
    return db_city


def updateCity(db: Session, id: schemas.City, title: schemas.CityBase):
    db_city = getCity(db=db)
    db_city.id = id
    db_city.name = title
    db.commit()
    db.refresh(db_city)
    return db_city


def deleteCity(db: Session):
    db_city = getCity(db=db)
    db.delete(db_city)
    db.commit()
