# Запрос 5. 
# Для Олимпийских игр 2000 года найдите 5 стран с минимальным соотношением количества групповых медалей к численности населения.
from base import *

with engine.connect() as conn:
    res = conn.execute('''
        with teammedals as (select e.event_id, o.country_id, count(*)
                            from events e,
                                olympics o
                            where e.olympic_id = o.olympic_id
                            and e.is_team_event = true
                            group by e.event_id, o.country_id),
            temp as (select c.name, count(*) / cast(c.population as float) as ratio
                    from teammedals im,
                        events e,
                        countries c,
                        olympics o
                    where e.event_id = im.event_id
                        and e.olympic_id = o.olympic_id
                        and o.year = 2000
                        and im.country_id = c.country_id
                    group by c.name, c.population)
        select name
        from temp t1
        where 5 > (select count(*) from temp t2 where t2.ratio < t1.ratio)
        ''')
    for row in res:
        print(row)