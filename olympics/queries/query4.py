# Запрос 4. 
# В какой стране был наибольший процент игроков (из перечисленных в наборе данных), чьи имена начинались с гласной?
from base import *

with engine.connect() as conn:
    res = conn.execute('''
        with temp as (select c1.country_id, cast(c2.num_players as float) / c1.num_players as ratio
                    from (select country_id, count(player_id) as num_players from players group by country_id) c1,
                        (select country_id, count(player_id) as num_players
                            from players
                            where substr(name, 1, 1)
                                    in ('A', 'E', 'O', 'I', 'U')
                            group by country_id) c2
                    where c1.country_id = c2.country_id)
        select c.name
        from temp t,
            countries c
        where ratio = (select max(ratio) from temp)
        and t.country_id = c.country_id
        ''')
    for row in res:
        print(row)