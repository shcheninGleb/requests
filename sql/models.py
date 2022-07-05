from sqlalchemy import Column, String
from database import Base


class City(Base):
    __tablename__ = "Cities"
    id = Column(String, index=True)
    title = Column(String, index=True)
