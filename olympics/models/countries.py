# create table Countries (
#     name char(40),
#     country_id char(3) unique,
#     area_sqkm integer,
#     population integer
# );

from sqlalchemy import Column, Integer, String
from models.base import Base

class Countries(Base):
    __tablename__ = 'countries'

    name = Column(String(100))
    country_id = Column(String(3), primary_key=True)
    area_sqkm = Column(Integer())
    population = Column(Integer())