# create table Players (
#     name char(40),
#     player_id char(10) unique,
#     country_id char(3),
#     birthdate date,
#     foreign key (country_id) references Countries(country_id)
# );

from sqlalchemy import Column, Integer, String, Date, ForeignKey
from models.base import Base
from models.countries import Countries

class Players(Base):
    __tablename__ = 'players'

    name = Column(String(40))
    player_id = Column(String(10), primary_key=True)
    country_id = Column(ForeignKey(Countries.country_id, ondelete='cascade'))
    birthdate = Column(Date())