# Запрос 1. 
# Для Олимпийских игр 2004 года сгенерируйте список (год рождения, количество игроков, количество золотых медалей), 
# содержащий годы, в которые родились игроки, количество игроков, родившихся в каждый из этих лет, 
# которые выиграли по крайней мере одну золотую медаль, и количество золотых медалей, завоеванных игроками, родившимися в этом году.
from base import *

with engine.connect() as conn:
    res = conn.execute('''
        select extract(year from birthdate) as birthday, count(medal), count(distinct players.player_id)
        from players,
            results,
            events,
            olympics
        where players.player_id = results.player_id
        and events.olympic_id = olympics.olympic_id
        and events.event_id = results.event_id
        and medal = 'GOLD'
        and olympics.year = 2004
        group by extract(year from birthdate)
        ''')
    for row in res:
        print(row)