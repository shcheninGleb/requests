from pydantic import BaseModel


class CityBase(BaseModel):
    title: str


class CityCreate(CityBase):
    pass


class City(CityBase):
    id: str


class Config:
    orm_mode = True
