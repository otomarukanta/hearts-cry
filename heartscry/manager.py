from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker
from heartscry.model.url import ScrapedURL, init_all
import json


class UrlManager():

    DB_JSON = './conf/db.json'

    def __init__(self):
        self.init_engine()
        self.Session = sessionmaker(bind=self.engine)

    def init_engine(self):
        with open(self.DB_JSON) as f:
            self.db_conf = json.load(f)
        self.engine = create_engine(URL(**self.db_conf))

    def init_url_tables(self):
        init_all(self.engine)

    def insert_urls(self, urls):
        session = self.Session()
        objs = [ScrapedURL(url=url, scraped=False) for url in urls]
        session.bulk_save_objects(objs)
