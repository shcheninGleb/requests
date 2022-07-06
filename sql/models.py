from sqlalchemy import Column, String
from sql.database import Base


class City(Base):
    __tablename__ = "city"
    id = Column(String, primary_key=True)
    name = Column(String)
