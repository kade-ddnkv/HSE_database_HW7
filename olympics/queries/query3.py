# Запрос 3. 
# Найдите всех игроков, которые выиграли хотя бы одну медаль (GOLD, SILVER и BRONZE) 
# на одной Олимпиаде. (player-name, olympic-id).
from base import *

with engine.connect() as conn:
    res = conn.execute('''
        (SELECT players.name, olympic_id
        from events,
            results,
            players
        where players.player_id = results.player_id
        and events.event_id = results.event_id
        and medal like '%%GOLD%%')
        intersect
        (SELECT players.name, olympic_id
        from events,
            results,
            players
        where players.player_id = results.player_id
        and events.event_id = results.event_id
        and medal like '%%SILVER%%')
        intersect
        (SELECT players.name, olympic_id
        from events,
            results,
            players
        where players.player_id = results.player_id
        and events.event_id = results.event_id
        and medal like '%%BRONZE%%')
        ''')
    for row in res:
        print(row)