import sqlite3
from logging import getLogger


class UrlDB:
    def __init__(self):
        self.conn = sqlite3.connect('urls.db')
        self.cur = self.conn.cursor()
        self.logger = getLogger(__name__)

    def init_table(self, table):
        self.logger.info("Initialize table '{}'".format(table))
        self.cur.execute('DROP TABLE IF EXISTS {}'.format(table))
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS {} (
                url TEXT PRIMARY KEY,
                scraped INTEGER
            )
        '''.format(table))

        self.conn.commit()

    def insert_url(self, table, url):
        try:
            self.logger.info("Inserting url '{}' into '{}'".format(url, table))
            self.cur.execute(
                    'INSERT INTO {} VALUES (?, 0)'.format(table), (url,))
        except sqlite3.IntegrityError as e:
            self.logger.error(e)

        self.conn.commit()
