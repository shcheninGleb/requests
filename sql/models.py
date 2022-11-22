from sqlalchemy import Column, String, DateTime
from sql.database import Base
from datetime import datetime


class City(Base):
    __tablename__ = "city"
    id = Column(String, primary_key=True)
    name = Column(String)
    created_date = Column(DateTime, default=datetime.utcnow)
    updated_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.now)
