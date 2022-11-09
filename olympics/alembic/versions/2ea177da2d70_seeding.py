"""Seeding

Revision ID: 2ea177da2d70
Revises: 732f374d616e
Create Date: 2022-11-09 17:27:49.149288

"""
from alembic import op
from faker import Faker
from models.countries import Countries
from models.olympics import Olympics
from models.players import Players
from models.events import Events
from models.results import Results


# revision identifiers, used by Alembic.
revision = '2ea177da2d70'
down_revision = '3fd0760aeef7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # meta = MetaData(bind=op.get_bind())
    # meta.reflect(only=('countries', 'olympics'))
    # countries = Table('countries', meta)
    # olympics = Table('olympics', meta)

    fake = Faker()

    op.bulk_insert(Countries.__table__,
    [{'name': fake.country()
    , 'country_id': fake.unique.random_int(max=999)
    , 'area_sqkm': fake.random_int()
    , 'population': fake.random_int()}
    for _ in range(15)]
    )

    conn = op.get_bind()
    res = conn.execute("select country_id from countries").fetchall()
    country_ids = [x[0] for x in res]

    op.bulk_insert(Olympics.__table__,
    [{
        'olympic_id': fake.unique.random_int(max=9999999)
        , 'country_id': fake.random_element(elements=country_ids)
        , 'city': fake.city()
        , 'year': fake.random_element(elements=(2000, 2004, 2008, 2012))
        , 'startdate': fake.date()
        , 'enddate': fake.date()
    }for _ in range(50)])

    op.bulk_insert(Players.__table__,
    [{
        'name': fake.name()
        , 'player_id': fake.unique.random_int(max=9999999999)
        , 'country_id': fake.random_element(elements=country_ids)
        , 'birthdate': fake.date()
    }for _ in range(10000)])

    res = conn.execute("select olympic_id from olympics").fetchall()
    olympic_ids = [x[0] for x in res]

    op.bulk_insert(Events.__table__,
    [{
        'event_id': fake.unique.random_int(max=9999999)
        , 'name': fake.name()
        , 'eventtype': fake.word()
        , 'olympic_id': fake.random_element(elements=olympic_ids)
        , 'is_team_event': fake.boolean()
        , 'num_players_in_team': fake.random_int(max=10)
        , 'result_noted_in': fake.text(max_nb_chars=70)
    }for _ in range(250)])

    res = conn.execute("select event_id from events").fetchall()
    event_ids = [x[0] for x in res]
    res = conn.execute("select player_id from players").fetchall()
    player_ids = [x[0] for x in res]

    s = set()
    def pair_key_return():
        i = 0
        while i == 0 or (a, b) in s:
            a = fake.random_element(elements=event_ids)
            b = fake.random_element(elements=player_ids)
            i += 1
        s.add((a, b))
        return {
            'event_id': a
            , 'player_id': b
            , 'medal': fake.random_element(elements=('BRONZE', 'SILVER', 'GOLD'))
            , 'result': fake.random_int() / fake.random_int(min=1)
        }

    op.bulk_insert(Results.__table__,
    [pair_key_return() for _ in range(5000)])


def downgrade() -> None:
    # op.execute('truncate table olympics.public.countries cascade')

    op.execute(Countries.__table__.delete())
    op.execute(Olympics.__table__.delete())
    op.execute(Players.__table__.delete())
    op.execute(Events.__table__.delete())
    op.execute(Results.__table__.delete())
