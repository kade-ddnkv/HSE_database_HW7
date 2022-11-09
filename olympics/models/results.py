# create table Results (
#     event_id char(7),
#     player_id char(10),
#     medal char(7),
#     result float,
#     foreign key (event_id) references Events(event_id),
#     foreign key (player_id) references players(player_id)
# );

from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float
from models.base import Base
from models.players import Players
from models.events import Events

class Results(Base):
    __tablename__ = 'results'

    event_id = Column(ForeignKey(Events.event_id, ondelete='cascade'), primary_key=True)
    player_id = Column(ForeignKey(Players.player_id, ondelete='cascade'), primary_key=True)
    medal = Column(String(7))
    result = Column(Float())