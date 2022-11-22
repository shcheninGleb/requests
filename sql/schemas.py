from pydantic import BaseModel, validator
from datetime import datetime
from typing import Optional


class CityBase(BaseModel):
    name: str


class City(CityBase):
    id: str


class DateTimeModel(BaseModel):
    created_date: Optional[datetime]
    updated_date: Optional[datetime]

    @validator("created_date", "updated_date", pre=True, always=True)
    def default_datetime(cls, value: datetime) -> datetime:
        return value or datetime.now()


class CityCreate(City, DateTimeModel):
    pass


class Config:
    orm_mode = True
