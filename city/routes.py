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
def create_city_api(
        item: schemas.CityCreate, db: Session = Depends(dependency.get_db)
):
    city = crud.create_city(db, item)
    return {'id': city.id, 'name': city.name}


@router.get("/list", response_model=List[schemas.City])
def read_cities(
        skip: int = 0, limit: int = 100, db: Session = Depends(dependency.get_db)
):
    items = crud.get_city(db, skip=skip, limit=limit)
    return list(map(lambda i: {'id': i.id, 'name': i.name}, items))
