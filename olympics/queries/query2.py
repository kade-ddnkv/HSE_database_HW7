# Запрос 2. 
# Перечислите все индивидуальные (не групповые) соревнования, в которых была ничья в счете, 
# и два или более игрока выиграли золотую медаль.
from base import *

with engine.connect() as conn:
    res = conn.execute('''
        select name, olympic_id
        from events
        where is_team_event = false
        and event_id in (select event_id
                        from results
                        where medal like '%%GOLD%%'
                        group by event_id
                        having count(medal) > 1)
        ''')
    for row in res:
        print(row)