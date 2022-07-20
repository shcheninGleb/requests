from pydantic import BaseModel


class CityBase(BaseModel):
    name: str


class City(CityBase):
    id: str


class CityCreate(City):
    pass


class Config:
    orm_mode = True
