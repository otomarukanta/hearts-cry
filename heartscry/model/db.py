from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import String, DateTime, Integer
from sqlalchemy.dialects import postgresql

DeclarativeBase = declarative_base()


def init_all_table(engine):
    """"""
    DeclarativeBase.metadata.drop_all(engine)
    DeclarativeBase.metadata.create_all(engine)


class Race(DeclarativeBase):
    __tablename__ = "race_meta"

    race_id = Column(String, primary_key=True)
    race_name = Column(String)
    race_datetime = Column(DateTime)
    race_no = Column(Integer)
    race_days = Column(Integer)
    race_weeks = Column(Integer)
    race_grade = Column(String)

    track_meter = Column(Integer)
    track_place = Column(String)
    track_rotation = Column(String)
    track_type = Column(String)
    track_side = Column(String)
    track_surface = Column(String)
    track_condition = Column(String)
    track_weather = Column(String)

    cond_intl = Column(String)
    cond_age = Column(String)
    cond_jockey = Column(String)
    cond_local = Column(String)
    cond_weight = Column(String)

    prize1 = Column(Integer)
    prize2 = Column(Integer)
    prize3 = Column(Integer)
    prize4 = Column(Integer)
    prize5 = Column(Integer)


class Payoff(DeclarativeBase):
    __tablename__ = "race_payoff"

    race_id = Column(String, primary_key=True)
    kind = Column(String, primary_key=True)
    odds_id = Column(String, primary_key=True)
    comb = Column(postgresql.ARRAY(Integer))
    yen = Column(Integer)
    popularity = Column(String)


class Result(DeclarativeBase):
    __tablename__ = "race_result"

    race_id = Column(String, primary_key=True)
    row = Column(String, primary_key=True)
    fp = Column(String)
    bk = Column(String)
    pp = Column(String)
    horse_id = Column(String)
    horse_sex = Column(String)
    horse_age = Column(String)
    jockey_id = Column(String)
    time = Column(String)
    margin = Column(String)
    positions = Column(String)
    l3f = Column(String)
    jockey_weight = Column(String)
    horse_weight = Column(String)
    fav = Column(String)
    odds = Column(String)
    blinker = Column(String)
    trainer_id = Column(String)
