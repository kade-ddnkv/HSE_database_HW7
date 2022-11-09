# create table Olympics (
#     olympic_id char(7) unique,
#     country_id char(3),
#     city char(50),
#     year integer,
#     startdate date,
#     enddate date,
#     foreign key (country_id) references Countries(country_id)
# );

from sqlalchemy import Column, Integer, String, Date, ForeignKey
from models.base import Base
from models.countries import Countries

class Olympics(Base):
    __tablename__ = 'olympics'

    olympic_id = Column(String(7), primary_key=True)
    country_id = Column(ForeignKey(Countries.country_id, ondelete='cascade'))
    city = Column(String(100))
    year = Column(Integer())
    startdate = Column(Date())
    enddate = Column(Date())