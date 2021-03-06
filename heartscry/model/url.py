from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import String, Boolean

DeclarativeBase = declarative_base()


def init_all(engine):
    DeclarativeBase.metadata.drop_all(engine)
    DeclarativeBase.metadata.create_all(engine)


class TargetURL(DeclarativeBase):
    __tablename__ = "target_urls"

    url = Column(String, primary_key=True)
    scraped = Column(Boolean)
