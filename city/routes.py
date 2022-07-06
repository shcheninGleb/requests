from sql import crud
from sql import schemas
from fastapi import APIRouter, Depends
import dependency
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(
    prefix="/api/city",
)


@router.post("", response_model=schemas.City)
def createCityApi(
        item: schemas.CityCreate, db: Session = Depends(dependency.getDb)
):
    return crud.createCity(db=db, item=item)


@router.get("/list", response_model=List[schemas.City])
def readCities(
        skip: int = 0, limit: int = 100, db: Session = Depends(dependency.getDb)
):
    items = crud.getCity(db, skip=skip, limit=limit)
    return list(map(lambda i: {'id': i.id, 'name': i.name}, items))
