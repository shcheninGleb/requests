from typing import List

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def getDb():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.post("/api/city", response_model=schemas.City)
def createCityApi(
    item: schemas.CityCreate, db: Session = Depends(getDb)
):
    return crud.createCity(db=db, item=item)


@app.get("/city/", response_model=List[schemas.City])
def readCities(skip: int = 0, limit: int = 100, db: Session = Depends(getDb)):
    items = crud.getCity(db, skip=skip, limit=limit)
    return items
