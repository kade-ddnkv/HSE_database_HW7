# create table Events (
#     event_id char(7) unique,
#     name char(40),
#     eventtype char(20),
#     olympic_id char(7),
#     is_team_event integer check (is_team_event in (0, 1)),
#     num_players_in_team integer,
#     result_noted_in char(100),
#     foreign key (olympic_id) references Olympics(olympic_id)
# );

from sqlalchemy import Column, Integer, String, Date, ForeignKey, Boolean
from models.base import Base
from models.olympics import Olympics

class Events(Base):
    __tablename__ = 'events'

    event_id = Column(String(7), primary_key=True)
    name = Column(String(40))
    eventtype = Column(String(20))
    olympic_id = Column(ForeignKey(Olympics.olympic_id, ondelete='cascade'))
    is_team_event = Column(Boolean())
    num_players_in_team = Column(Integer())
    result_noted_in = Column(String(100))